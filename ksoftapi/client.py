# -*- coding: utf-8 -*-
import asyncio

from .apis import bans, images
from .http import HttpClient


class Client:
    """
    .. _aiohttp session: https://aiohttp.readthedocs.io/en/stable/client_reference.html#client-session

    Client object for KSOFT.SI API.
    Represents a client connection that connects to ksoft.si.

    Parameters
    -------------
    api_key: :class:`str`
        Your ksoft.si api token.
        Specify different base url.
    **loop: asyncio loop
        Your asyncio loop.
    """

    def __init__(self, api_key: str, loop=None):
        self._loop = loop or asyncio.get_event_loop()
        self.api_key = api_key
        self.http = HttpClient(authorization=self.api_key, loop=self._loop)

        self._bans_api = bans.Ban(self)
        self._images_api = images.Image(self)

    @property
    def bans(self):
        return self._bans_api

    @property
    def images(self):
        return self._images_api
