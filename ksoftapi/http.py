# -*- coding: utf-8 -*-
import logging
import sys

import aiohttp

from . import __version__

logger = logging.getLogger()


class Route:
    def __init__(self, method, path, subpath: str = '', **parameters):
        self.path = subpath + path
        self.method = method
        self.url = (self.BASE + self.path).format(**parameters)

    @classmethod
    def trola(cls, method, path, **parameters):
        return cls(method, path, 'trola', **parameters)


class HttpClient(object):
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
        payload = {'json': body} if type(body) is dict else {'data': body}
        async with self._session.post(self.BASE + self.path, **payload, headers=merged_headers) as res:
            if to_json:
                return await res.json()

            return await res.text()

    async def delete(self, path: str, params=None, headers=None, to_json=True):
        merged_headers = {**headers, **self._default_headers} if headers else self._default_headers
        async with self._session.delete(self.BASE + path, params=params, headers=merged_headers) as res:
            if to_json:
                return await res.json()

            return await res.text()

    #  TODO:
    #   - Perhaps add status code checks?

    # async def download_get(self, url, filename, params=None, headers=None, verify=True):
    #     headers = headers or {}
    #     headers.update(self.headers)
    #     async with self.session.get(url, params=params, headers=headers) as response:
    #         if response.status != 200:
    #             raise Forbidden
    #         with open(filename, 'wb') as f_handle:
    #             while True:
    #                 chunk = await response.content.read(1024)
    #                 if not chunk:
    #                     break
    #                 f_handle.write(chunk)
    #         await response.release()

    # async def download_post(self, url, filename, data=None, json=None, headers=None, verify=True):
    #     headers = headers or {}
    #     headers.update(self.headers)
    #     if json is not None:
    #         async with self.session.post(url, json=json, headers=headers) as response:
    #             if response.status != 200:
    #                 raise Forbidden
    #             with open(filename, 'wb') as f_handle:
    #                 while True:
    #                     chunk = await response.content.read(1024)
    #                     if not chunk:
    #                         break
    #                     f_handle.write(chunk)
    #             await response.release()
    #     else:
    #         async with self.session.post(url, data=data, headers=headers) as response:
    #             if response.status != 200:
    #                 raise Forbidden
    #             with open(filename, 'wb') as f_handle:
    #                 while True:
    #                     chunk = await response.content.read(1024)
    #                     if not chunk:
    #                         break
    #                     f_handle.write(chunk)
    #             await response.release()
