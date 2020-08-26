from typing import List, Union

from ..errors import NoResults
from ..models import Location, Weather


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

    async def basic_weather(self, location: str, report_type: str = "currently", units: str = "auto",
                            lang: str = "en", icon_pack: str = "original") -> Union[Weather, List[Weather]]:
        """|coro|
        Provides weather information for the given location.

        Parameters
        ------------
        location: str
            The location to get the weather from.
        report_type: str
            The type of report to get. Defaults to current if not set.
        units: str
            The units the information should be shown in.
        lang: str
            The language the information should be shown in. Defaults to english if not set.
        icon_pack: str
            Select the icon pack. Defaults to original if not set.

        Returns
        -------
        Union[:class:`Weather`, List[:class:`Weather`]]
            A list of :class:`Weather` if ``more`` is True, otherwise a :class:`Weather`.

        Raises
        ------
        :class:`NoResults`
        """

        r = await self._client.http.get('/kumo/weather/{}'.format(report_type),
                                        params={"q": location, "units": units, "lang": lang, "icons": icon_pack})

        if r.get('code', 200) == 404:
            raise NoResults

        result = r['data']
        if isinstance(result, list):
            return [Weather(r) for r in result]

        return Weather(result)

    async def advanced_weather(self, latitude: float, longitude: float, report_type: str = "currently", units: str = "auto",
                               lang: str = "en", icon_pack: str = "original") -> Union[Weather, List[Weather]]:
        """|coro|
        Provides weather information for the given location.

        Parameters
        ------------
        latitude: float
            The latitude coordinate
        longitude: float
            The longitude coordinate
        report_type: str
            The type of report to get. Defaults to current if not set.
        units: str
            The units the information should be shown in.
        lang: str
            The language the information should be shown in. Defaults to english if not set.
        icon_pack: str
            Select the icon pack. Defaults to original if not set.

        Returns
        -------
        Union[:class:`Weather`, List[:class:`Weather`]]
            A list of :class:`Weather` if ``more`` is True, otherwise a :class:`Weather`.

        Raises
        ------
        :class:`NoResults`
        """

        r = await self._client.http.get('/kumo/weather/{},{}/{}'.format(latitude, longitude, report_type),
                                        params={"units": units, "lang": lang, "icons": icon_pack})

        if r.get('code', 200) == 404:
            raise NoResults

        result = r['data']
        if isinstance(result, list):
            return [Weather(r) for r in result]

        return Weather(result)
