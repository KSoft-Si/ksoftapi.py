from typing import List

from ..errors import NoResults
from ..models import LyricResult, Recommendation


class Music:
    def __init__(self, client):
        self._client = client

    async def lyrics(self, query: str, text_only: bool = False, clean_up: bool = True, limit: int = 10) -> List[LyricResult]:
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
        r = await self._client.http.get('/lyrics/search', params={'q': query, 'text_only': text_only, 'limit': limit,
                                                                  'clean_up': clean_up})
        results = r['data']

        if not results:
            raise NoResults

        return [LyricResult(lr) for lr in results]

    async def recommendations(self, tracks: list, provider: str, youtube_token: str = None, limit: int = 5,
                              recommend_type: str = None) -> List[Recommendation]:
        """|coro|
        Fetches a list of tracks that are related to the list of given tracks.

        Parameters
        ------------
        tracks: list
            A list of strings. The strings can be one of: youtube links, youtube ids, youtube titles, or spotify ids.
        provider: str
            The type of strings that were passed to tracks. This is either "youtube" (links), "youtube_ids",
            "youtube_titles" or "spotify".
        youtube_token: str
            (optional) An YouTube API token, should you wish to use your own key.
        limit: int
            (optional) The maximum number of results that should be returned (1-5).
        recommend_type: str
            (optional) Which data type to return. This can be "track", "youtube_link" or "youtube_id".

        Returns
        -------
        list
            A list of :class:`Recommendation`

        Raises
        ------
        :class:`NoResults`
        """
        payload = {'tracks': tracks, 'provider': provider, 'limit': limit}

        if youtube_token is not None:
            payload['youtube_token'] = youtube_token

        if recommend_type is not None:
            payload['recommend_type'] = recommend_type

        r = await self._client.http.post('/music/recommendations', body=payload)
        results = r['tracks']

        if not results:
            raise NoResults

        return [Recommendation(r) for r in results]
