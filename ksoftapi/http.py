# -*- coding: utf-8 -*-
import logging
import sys

import aiohttp

from . import __version__  # pylint: disable=R0401

logger = logging.getLogger()


# class Route:
#     @classmethod
#     def trola(cls, method, path, **parameters):
#         return cls(method, path, 'trola', **parameters)


class HttpClient:
    BASE = 'https://api.ksoft.si'

    def __init__(self, authorization, loop):
        self._default_headers = {
            'Authorization': 'NANI ' + authorization,
            'User-Agent': 'KSoftApi.py/{} (https://github.com/KSoft-Si/ksoftapi.py)'.format(__version__),
            'X-Powered-By': 'aiohttp {}/Python {}'.format(aiohttp.__version__, sys.version)
        }
        self._session = aiohttp.ClientSession(loop=loop)

    async def get(self, path: str, params=None, headers=None, to_json=True):
        merged_headers = {**headers, **self._default_headers} if headers else self._default_headers
        async with self._session.get(self.BASE + path, params=params, headers=merged_headers) as res:
            if to_json:
                return await res.json()

            return await res.text()

    async def post(self, path: str, body=None, headers=None, to_json=True):
        merged_headers = {**headers, **self._default_headers} if headers else self._default_headers
        payload = {'json': body} if isinstance(body, dict) else {'data': body}
        async with self._session.post(self.BASE + path, **payload, headers=merged_headers) as res:
            if to_json:
                return await res.json()

            return await res.text()

    async def delete(self, path: str, params=None, headers=None, to_json=True):
        merged_headers = {**headers, **self._default_headers} if headers else self._default_headers
        async with self._session.delete(self.BASE + path, params=params, headers=merged_headers) as res:
            if to_json:
                return await res.json()

            return await res.text()

    # - Perhaps add status code checks?
