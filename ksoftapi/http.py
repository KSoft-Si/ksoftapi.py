# -*- coding: utf-8 -*-

import asyncio
import logging
import sys
import traceback

import aiohttp

from . import __version__
from .errors import *

logger = logging.getLogger()


class Route:
    def __init__(self, method, path, subpath: str = '', **parameters):
        self.path = subpath + path
        self.method = method
        self.url = (self.BASE + self.path).format(**parameters)

    @classmethod
    def meme(cls, method, path, **parameters):
        return cls(method, path, 'meme', **parameters)

    @classmethod
    def bans(cls, method, path, **parameters):
        return cls(method, path, 'bans', **parameters)

    @classmethod
    def trola(cls, method, path, **parameters):
        return cls(method, path, 'trola', **parameters)


class HttpClient(object):
    BASE = 'https://api.ksoft.si'

    def __init__(self, authorization, loop=asyncio.get_event_loop(), bot=None):
        self._default_headers = {
            'Authorization': 'NANI ' + authorization,
            'User-Agent': 'KSoftApi.py/{} (https://github.com/KSoft-Si/ksoftapi.py)'.format(__version__),
            'X-Powered-By': 'aiohttp {}/Python {}'.format(aiohttp.__version__, sys.version)
        }
        self._bot = bot
        self._session = aiohttp.ClientSession(loop=loop)

    async def get(self, path: str, params=None, headers=None, to_json=False):
        merged_headers = {**headers, **self._default_headers} if headers else self._default_headers
        async with self.session.get(self.BASE + path, params=params, headers=merged_headers) as res:
            if to_json:
                return await res.json()

            return await res.text()

    async def post(self, path: str, body=None, headers=None, to_json=False):
        merged_headers = {**headers, **self._default_headers} if headers else self._default_headers
        payload = {'json': body} if type(body) is dict else {'data': body}
        async with self.session.post(self.BASE + self.path, **payload, headers=merged_headers) as res:
            if to_json:
                return await res.json()

            return await res.text()

    async def delete(self, path: str, params=None, headers=None, to_json=False):
        merged_headers = {**headers, **self._default_headers} if headers else self._default_headers
        async with self.session.delete(self.BASE + path, params=params, headers=merged_headers) as res:
            if to_json:
                return await res.json()

            return await res.text()

    async def _request(self, route: Route, params=None, data=None, json=None, headers=None):
        url = route.url
        method = route.method
        if method == "POST":
            return await self.post(url, data=data, json=json, headers=headers)
        elif method == "GET":
            return await self.get(url, params=params, headers=headers)
        elif method == "DELETE":
            return await self.delete(url, params=params, headers=headers)
        else:
            raise InvalidMethod

    async def download_get(self, url, filename, params=None, headers=None, verify=True):
        headers = headers or {}
        headers.update(self.headers)
        async with self.session.get(url, params=params, headers=headers) as response:
            if response.status != 200:
                raise Forbidden
            with open(filename, 'wb') as f_handle:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f_handle.write(chunk)
            await response.release()

    async def download_post(self, url, filename, data=None, json=None, headers=None, verify=True):
        headers = headers or {}
        headers.update(self.headers)
        if json is not None:
            async with self.session.post(url, json=json, headers=headers) as response:
                if response.status != 200:
                    raise Forbidden
                with open(filename, 'wb') as f_handle:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f_handle.write(chunk)
                await response.release()
        else:
            async with self.session.post(url, data=data, headers=headers) as response:
                if response.status != 200:
                    raise Forbidden
                with open(filename, 'wb') as f_handle:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f_handle.write(chunk)
                await response.release()
