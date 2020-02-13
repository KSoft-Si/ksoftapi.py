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

        :return: :class:`ksoftapi.data_objects.Image`
        """
        r = await self._client.http.get('/images/random-image', params={'tag': tag, 'nsfw': nsfw})
        return Image(r)

    async def random_meme(self) -> RedditImage:
        """|coro|
        This function gets a random meme from multiple sources from reddit.

        :return: :class:`ksoftapi.data_objects.RedditImage`
        """
        r = await self._client.http.get('/images/random-meme')
        return RedditImage(**r)

    async def random_aww(self) -> RedditImage:
        """|coro|
        This function gets a random cute pictures from multiple sources from reddit.

        :return: :class:`ksoftapi.data_objects.RedditImage`
        """
        r = await self._client.http.get('/images/random-aww')
        return RedditImage(**r)

    async def random_wikihow(self) -> WikiHowImage:
        """|coro|
        This function gets a random WikiHow image.

        :return: :class:`ksoftapi.data_objects.WikiHowImage`
        """
        r = await self._client.http.get('/images/random-wikihow')
        return WikiHowImage(r)

    async def random_reddit(self, subreddit: str) -> RedditImage:
        """|coro|
        This function gets a random post from specified subreddit.

        :return: :class:`ksoftapi.data_objects.RedditImage`
        """
        r = await self._client.http.get('/images/rand-reddit/{}'.format(subreddit))
        return RedditImage(r)

    async def tags(self) -> TagCollection:
        """|coro|
        This function gets all available tags on the api.

        :return: :class:`ksoftapi.data_objects.TagCollection`
        """
        r = await self._client.http.get('/images/tags')
        return TagCollection(r)
