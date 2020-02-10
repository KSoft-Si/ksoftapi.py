class Random:
    def __init__(self, client):
        self._client = client

# async def random_image(self, tag: str, nsfw: bool = False) -> Image:
#         """|coro|
#         This function gets a random image from the specified tag.

#         Parameters
#         ------------
#         tag: :class:`str`
#             Image tag from string.
#         nsfw: :class:`bool`
#             If to display NSFW images.

#         :return: :class:`ksoftapi.data_objects.Image`
#         """
#         g = await self.http.request(Route.meme("GET", "/random-image"), params={"tag": tag, "nsfw": nsfw})
#         return Image(**g)

#     async def random_meme(self) -> RedditImage:
#         """|coro|
#         This function gets a random meme from multiple sources from reddit.

#         :return: :class:`ksoftapi.data_objects.RedditImage`
#         """
#         g = await self.http.request(Route.meme("GET", "/random-meme"))
#         return RedditImage(**g)

#     async def random_aww(self) -> RedditImage:
#         """|coro|
#         This function gets a random cute pictures from multiple sources from reddit.

#         :return: :class:`ksoftapi.data_objects.RedditImage`
#         """
#         g = await self.http.request(Route.meme("GET", "/random-aww"))
#         return RedditImage(**g)

#     async def random_wikihow(self) -> WikiHowImage:
#         """|coro|
#         This function gets a random WikiHow image.

#         :return: :class:`ksoftapi.data_objects.WikiHowImage`
#         """
#         g = await self.http.request(Route.meme("GET", "/random-wikihow"))
#         return WikiHowImage(**g)

#     async def random_reddit(self, subreddit: str) -> RedditImage:
#         """|coro|
#         This function gets a random post from specified subreddit.

#         :return: :class:`ksoftapi.data_objects.RedditImage`
#         """
#         g = await self.http.request(Route.meme("GET", "/rand-reddit/{subreddit}", subreddit=subreddit))
#         return RedditImage(**g)
