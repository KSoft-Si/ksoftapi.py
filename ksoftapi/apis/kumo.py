from typing import List, Union

from ..errors import NoResults
from ..models import Location


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
