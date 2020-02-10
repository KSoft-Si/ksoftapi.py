from itertools import count

from errors import APIError
from models import BanInfo, PaginatorListing


class Ban:
    def __init__(self, client):
        self._client = client

    async def __aiter__(self):
        for page in count(start=1):
            r = await self._client.http.get('/bans/list', params={'page': page})

            for ban in r['data']:
                yield BanInfo(**ban)

            if r['next_page'] is None:
                break

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
