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
    BASE = 'https://api.ksoft.si/'

    def __init__(self, method, path, subpath: str = "", **parameters):
        self.path = subpath + path
        self.method = method
        url = (self.BASE + self.path)
        if parameters:
            self.url = url.format(**parameters)
        else:
            self.url = url

    @classmethod
    def meme(cls, method, path, **parameters):
        return cls(method, path, "meme", **parameters)

    @classmethod
    def bans(cls, method, path, **parameters):
        return cls(method, path, "bans", **parameters)

    @classmethod
    def trola(cls, method, path, **parameters):
        return cls(method, path, "trola", **parameters)


class krequest(object):
    def __init__(self, return_json=True, global_headers={}, loop=asyncio.get_event_loop(), **kwargs):
        self.bot = kwargs.get("bot", None)
        self.loop = loop
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.lowmem = kwargs.get("lowmem", False)
        self.headers = {
            "User-Agent": "{}ksoftapi.py/{} (Github: AndyTempel) KRequests/alpha "
                          "(Custom asynchronous HTTP wrapper)".format(
                f"{self.bot.user.username}/{self.bot.user.discriminator} " if self.bot else "", __version__),
            "X-Powered-By": "python/{} aiohttp/{}".format(sys.version, aiohttp.__version__)
        }
        self.return_json = return_json
        for name, value in global_headers:
            logger.info(f"KSOFTAPI Added global header {name}")
            self.headers.update({
                name: value
            })

        logger.debug(f"Here are global headers: {str(self.headers)}")

    async def _proc_resp(self, response):
        logger.debug(f"Request {response.method}: {response.url}")
        logger.debug(f"Response headers: {str(response.headers)}")
        if self.return_json:
            try:
                resp = await response.json()
                logger.debug(f"Response content: {str(resp)}")
                return resp
            except Exception:
                print(traceback.format_exc())
                print(response)
                resp = await response.text()
                logger.debug(f"Response content: {str(resp)}")
                return {}
        else:
            resp = await response.text()
            logger.debug(f"Response content: {str(resp)}")
            return resp

    async def request(self, route: Route, params=None, data=None, json=None, headers=None):
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

    async def get(self, url, params=None, headers=None, verify=True):
        headers = headers or {}
        headers.update(self.headers)
        async with self.session.get(url, params=params, headers=headers) as resp:
            r = await self._proc_resp(resp)
            await resp.release()
            return r

    async def delete(self, url, params=None, headers=None, verify=True):
        headers = headers or {}
        headers.update(self.headers)
        async with self.session.delete(url, params=params, headers=headers) as resp:
            r = await self._proc_resp(resp)
            await resp.release()
            return r

    async def post(self, url, data=None, json=None, headers=None, verify=True):
        headers = headers or {}
        headers.update(self.headers)
        if json is not None:
            async with self.session.post(url, json=json, headers=headers) as resp:
                r = await self._proc_resp(resp)
                await resp.release()
                return r
        else:
            async with self.session.post(url, data=data, headers=headers) as resp:
                r = await self._proc_resp(resp)
                await resp.release()
                return r

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
