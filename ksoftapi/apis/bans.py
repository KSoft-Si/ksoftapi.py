import logging
from asyncio import CancelledError, sleep
from itertools import count
from time import time

from ..errors import APIError
from ..events import BanEvent, UnBanEvent
from ..models import BanInfo, PaginatorListing

logger = logging.getLogger('ksoft/bans')


class Ban:
    def __init__(self, client):
        self._client = client
        self._hooks = []
        self._last_update = time() - 60 * 10

        self._listener_task = None

    async def __aiter__(self):
        for page in count(start=1):
            r = await self._client.http.get('/bans/list', params={'page': page})

            for ban in r['data']:
                yield BanInfo(**ban)

            if r['next_page'] is None:
                break

    async def _ban_checker(self):
        while self._hooks:
            try:
                r = await self.http.get('/bans/updates', params={'timestamp': self._last_update})
                self._last_update = time()
                for b in r['data']:
                    event = BanEvent(**b) if b['active'] else UnBanEvent(**b)
                    await self._dispatch_ban_event(event)
            except Exception as exc:
                logger.error('An error occurred within the ban update loop', exc_info=exc)
            finally:
                await sleep(60 * 5)

        try:
            self._listener_task.cancel()
        except CancelledError:
            pass

        self._listener_task = None

    async def _dispatch_ban_event(self, event):
        logger.debug('Dispatching event of type %s to %d hooks', event.__class__.__name__, len(self._ban_hook))
        for hook in self._ban_hook:
            try:
                await hook(event)
            except Exception as exc:
                logger.warning('Event hook "%s" encountered an exception', hook.__name__, exc_info=exc)

    def subscribe(self, hook):
        if hook not in self._hooks:
            logger.debug('Registered ban event hook with name %s', hook.__name__)
            self._hooks.append(hook)

        if len(self._hooks) > 0 and self._listener_task is None:
            self._listener_task = self._client._loop.create_task(self._ban_checker)

    def unsubscribe(self, hook):
        if hook in self._hooks:
            logger.debug('Unregistered ban event hook with name %s', hook.__name__)
            self._hooks.remove(hook)

    async def count(self) -> int:
        r = await self._client.http.get('/bans/list', params={"per_page": 1})
        return r['ban_count']

    async def paginator(self, page: int = 1, per_page: int = 20):
        r = await self._client.http.get('/bans/list', params={'per_page': per_page, 'page': page})
        return PaginatorListing(**r)

    async def add(self, user_id: int, reason: str, proof: str,
                  mod=None, user_name=None, user_discriminator=None, appeal_possible=None) -> bool:
        payload = {
            'user': user_id,
            'reason': reason,
            'proof': proof
        }

        if mod is not None:
            payload['mod'] = mod

        if user_name is not None:
            payload['user_name'] = user_name

        if user_discriminator is not None:
            payload['user_discriminator'] = user_discriminator

        if appeal_possible is not None:
            payload['appeal_possible'] = appeal_possible

        r = await self._client.http.post('/bans/add', data=payload)

        if r.get('success', False):
            return True

        raise APIError(**r)

    async def check(self, user_id: int) -> bool:
        r = await self._client.http.get('/bans/check', params={'user': user_id})

        if 'is_banned' in r:
            return r['is_banned']

        raise APIError(**r)

    async def info(self, user_id: int) -> BanInfo:
        r = await self._client.http.get('/bans/info', params={'user': user_id})

        if 'is_ban_active' in r:
            return BanInfo(**r)

        raise APIError(**r)

    async def remove(self, user_id: int) -> bool:
        r = await self.http.delete('/bans/remove', params={'user': user_id})

        if 'done' in r:
            return r['done']

        if r.get("done", None) is not None:
            return True
        else:
            raise APIError(**r)
