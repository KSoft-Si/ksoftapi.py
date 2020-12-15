from ..errors import NoResults
from ..models import Image, RedditImage, TagCollection, WikiHowImage


class Images:
    def __init__(self, client):
        self._client = client

    async def random_image(self, tag: str, nsfw: bool = False) -> Image:
        """|coro|
        This function gets a random image from the specified tag.

        Parameters
        ------------
        tag: :class:`str`
            The tag to fetch images of.
        nsfw: :class:`bool`
            Whether to include NSFW images.

        Returns
        -------
        :class:`Image`

        Raises
        ------
        :class:`NoResults`
        """
        r = await self._client.http.get('/images/random-image', params={'tag': tag, 'nsfw': nsfw})

        if r.get('code', 200) == 404:
            raise NoResults

        return Image(r)

    async def random_meme(self) -> RedditImage:
        """|coro|
        This function gets a random meme from multiple sources from reddit.

        Returns
        -------
        :class:`RedditImage`
        """
        r = await self._client.http.get('/images/random-meme')
        return RedditImage(r)

    async def random_aww(self) -> RedditImage:
        """|coro|
        This function gets a random cute pictures from multiple sources from reddit.

        Returns
        -------
        :class:`RedditImage`
        """
        r = await self._client.http.get('/images/random-aww')
        return RedditImage(r)

    async def random_wikihow(self) -> WikiHowImage:
        """|coro|
        This function gets a random WikiHow image.

        Returns
        -------
        :class:`WikiHowImage`
        """
        r = await self._client.http.get('/images/random-wikihow')
        return WikiHowImage(r)

    async def random_reddit(self, subreddit: str, remove_nsfw: bool = False, span: str = 'day') -> RedditImage:
        """|coro|
        This function gets a random post from specified subreddit.

        Parameters
        ----------
        subreddit: :class:`str`
            The subreddit to retrieve a random image from.
        remove_nsfw: :class:`bool`
            Whether to filter NSFW content.
        span: :class:`str`
            The timespan to collect images from.
            Can be one of "hour", "day", "week", "month", "year", or "all"

        Returns
        -------
        :class:`RedditImage`

        Raises
        ------
        :class:`NoResults`
            If the subreddit wasn't found.
        """
        r = await self._client.http.get('/images/rand-reddit/{}'.format(subreddit),
                                        params={'remove_nsfw': remove_nsfw, 'span': span})

        if r.get('code', 200) == 404:
            raise NoResults

        return RedditImage(r)

    async def tags(self) -> TagCollection:
        """|coro|
        This function gets all available tags on the api.

        Returns
        -------
        :class:`TagCollection`
        """
        r = await self._client.http.get('/images/tags')
        return TagCollection(r)

    async def get_image(self, snowflake: str) -> Image:
        """|coro|
        This function gets an image based on it's snowflake.

        Parameters
        ----------
        snowflake: :class:`str`
            The image snowflake (unique ID)

        Returns
        -------
        :class:`Image`
        """
        r = await self._client.http.get('/images/image/{}'.format(snowflake))

        if r.get('code', 200) == 404:
            raise NoResults

        return Image(r)

    async def search_tags(self, search: str) -> TagCollection:
        """|coro|
        This function searchs for tags.

        Parameters
        ----------
        search: :class:`str`
            The search query.

        Returns
        -------
        :class:`TagCollection`
        """
        r = await self._client.http.get('/images/tags/{}'.format(search))

        if r.get('code', 200) == 404:
            raise NoResults

        return TagCollection(r)

    async def random_nsfw(self, gifs: bool = False) -> RedditImage:
        """|coro|
        This function gets a random nsfw image.

        Parameters
        ----------
        gifs: :class:`bool`
            If gifs should be returned instead of images.

        Returns
        -------
        :class:`RedditImage`
        """
        r = await self._client.http.get('/images/random-nsfw', params={'gifs': gifs})
        return RedditImage(r)
