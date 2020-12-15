from typing import List, Union

from ..errors import NoResults
from ..models import Location, IPInfo, Currency


class Kumo:
    def __init__(self, client):
        self._client = client

    async def gis(self, location: str, fast: bool = False, more: bool = False, map_zoom: int = 12,
                  include_map: bool = False) -> Union[Location, List[Location]]:
        """|coro|
        Provides information and co-ordinates for the given location, and optionally, an image.

        Parameters
        ------------
        location: str
            The location to get information of.
        fast: bool
            Whether to sacrifice information for a faster response.
        more: bool
            Whether to return more than one location.
        map_zoom: int
            Sets the zoom level of the map. This option is ignored if fast is False.
        include_map: bool
            Whether to include an image of the map.

        Returns
        -------
        Union[:class:`Location`, List[:class:`Location`]]
            A list of :class:`Location` if ``more`` is True, otherwise a :class:`Location`.

        Raises
        ------
        :class:`NoResults`
        """
        r = await self._client.http.get('/kumo/gis', params={'q': location, 'fast': fast, 'more': more, 'map_zoom': map_zoom,
                                                             'include_map': include_map})

        if r.get('code', 200) == 404:
            raise NoResults

        result = r['data']
        if isinstance(result, list):
            return [Location(r) for r in result]

        return Location(result)

    async def geoip(self, ip: str):
        """|coro|
        Gets location data from the IP address.

        Parameters
        ----------
        ip: :class:`str`
            The ip address.

        Returns
        -------
        :class:`IPInfo`

        Raises
        ------
        :class:`NoResults`
        """
        r = await self._client.http.get('/kumo/geoip', params={'ip': ip})

        if r.get('code', 200) == 404:
            raise NoResults

        result = r['data']
        return IPInfo(result)

    async def currency(self, from_: str, to: str, value: str):
        """|coro|
        Convert a value from one currency to another.

        Parameters
        ----------
        from_: :class:`str`
            The original currency of the value.
            Should match https://en.wikipedia.org/wiki/ISO_4217#Active_codes
        to: :class:`str`
            The currency to convert to.
            Should match https://en.wikipedia.org/wiki/ISO_4217#Active_codes
        value: :class:`str`
            The value you want to convert.

        Returns
        -------
        :class:`Currency`

        Raises
        ------
        :class:`NoResults`
        """
        r = await self._client.http.get('/kumo/currency', params={'from': from_, 'to': to, 'value': value})

        if r.get('code', 200) == 404:
            raise NoResults

        result = r['data']
        return Currency(result)
