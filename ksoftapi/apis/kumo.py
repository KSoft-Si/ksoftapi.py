class Kumo:
    def __init__(self, client):
        self._client = client

    async def gis(self, location: str, fast: bool, more: bool, map_zoom: int, include_map: bool):
        """|coro|
        Fetches the lyrics for the given query.

        Parameters
        ------------
        query: str
            The lyrics search query.
        text_only: bool
            Whether to search for the query within the lyrics.
        clean_up: bool
            Whether the API should attempt to clean-up garbage in the query
            For example: strings like [Official Music Video], [Lyric Video] etc.
        limit: int
            The maximum number of results that should be returned.

        Returns
        -------
        list
            A list of :class:`LyricResult`

        Raises
        ------
        :class:`NoResults`
        """