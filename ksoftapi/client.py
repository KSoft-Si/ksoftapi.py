# -*- coding: utf-8 -*-
import asyncio

from .apis import ban, random
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

        self._ban_api = ban.Ban(self)
        self._random_api = random.Random(self)

    @property
    def bans(self):
        return self._ban_api

    @property
    def random(self):
        return self._random_api
