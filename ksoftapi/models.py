from typing import Dict, List


class BanInfo:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.discriminator = kwargs.get('discriminator')
        self.moderator_id = kwargs.get('moderator_id')
        self.reason = kwargs.get('reason')
        self.proof = kwargs.get('proof')
        self.is_ban_active = kwargs.get('is_ban_active')
        self.can_be_appealed = kwargs.get('can_be_appealed')
        self.timestamp = kwargs.get('timestamp')
        self.appeal_reason = kwargs.get('appeal_reason')
        self.appeal_date = kwargs.get('appeal_date')
        self.requested_by = kwargs.get('requested_by')
        self.exists = kwargs.get('exists')


class BanSimple:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.reason = kwargs.get("reason")
        self.proof = kwargs.get("proof")
        self.moderator_id = kwargs.get("moderator_id")
        self.active = kwargs.get("active")


class Image:
    def __init__(self, **kwargs):
        self.snowflake = kwargs.get('snowflake')
        self.url = kwargs.get('url')
        self.nsfw = kwargs.get('nsfw')
        self.tag = kwargs.get('tag')


class LyricResult:
    def __init__(self, data):
        self.artist: str = data.get('artist')
        self.artist_id: int = data.get('artist_id')
        self.album: str = data.get('album')
        self.album_ids: List[str] = data.get('album_ids').split(',')
        self.album_year: List[str] = data.get('album_year').split(',')
        self.name: str = data.get('name')
        self.lyrics: str = data.get('lyrics')
        self.search_str: str = data.get('search_str')
        self.album_art: str = data.get('album_art')
        self.popularity: int = data.get('popularity')
        self.id: str = data.get('id')
        self.search_score: float = data.get('search_score')


class PaginatorListing:
    def __init__(self, **kwargs):
        self.count = kwargs.get('ban_count')
        self.page_count = kwargs.get('page_count')
        self.per_page = kwargs.get('per_page')
        self.page = kwargs.get('page')
        self.on_page = kwargs.get('on_page')
        self.next_page = kwargs.get('next_page')
        self.previous_page = kwargs.get('previous_page')
        self.data = [BanInfo(**ban) for ban in kwargs.get('data')]


class Recommendation:
    def __init__(self, data):
        self.name: str = data['name']

        youtube = data['youtube']
        self.youtube_id: str = youtube['id']
        self.youtube_link: str = youtube['link']
        self.youtube_title: str = youtube['title']
        self.youtube_thumbnail: str = youtube['thumbnail']

        spotify = data['spotify']
        spotify_album = spotify['album']
        spotify_artists = spotify['artists']
        self.spotify_id: str = spotify['id']
        self.spotify_name: str = spotify['name']
        self.spotify_link: str = spotify['link']
        self.spotify_album_name: str = spotify_album['name']
        self.spotify_album_art: str = spotify_album['album_art']
        self.spotify_album_link: str = spotify_album['link']
        self.spotify_artists: Dict[str, str] = [
            {'name': artist['name'], 'link': artist['link']}
            for artist in spotify_artists
        ]


class RedditImage:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.image_url = kwargs.get('image_url')
        self.url = self.image_url
        self.source = kwargs.get('source')
        self.subreddit = kwargs.get('subreddit')
        self.upvotes = kwargs.get('upvotes')
        self.downvotes = kwargs.get('downvotes')
        self.comments = kwargs.get('comments')
        self.created_at = kwargs.get('created_at')
        self.nsfw = kwargs.get('nsfw')


class Tag:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.nsfw = kwargs.get('nsfw')

    def __str__(self):
        return self.name


class TagCollection:
    def __init__(self, **kwargs):
        self._raw = kwargs.get('models')
        self.models = [Tag(**t) for t in kwargs.get('models')]
        self.sfw_tags = kwargs.get('tags')
        self.nsfw_tags = kwargs.get('nsfw_tags', [])

    def __len__(self):
        return len(self.models)

    def __dict__(self):
        return self._raw

    def __getitem__(self, item):
        return next((item == t.name for t in self.models), None)

    def __iter__(self):
        for t in self.models:
            yield t

    def __str__(self):
        return ', '.join([t.name for t in self.models])

    def exists(self, name):
        return any(name == t.name for t in self.models)


class WikiHowImage:
    def __init__(self, **kwargs):
        self.url = kwargs.get('url')
        self.title = kwargs.get('title')
        self.nsfw = kwargs.get('nsfw')
        self.article_url = kwargs.get('article_url')
