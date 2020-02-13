from typing import Dict, List, Optional


class BanInfo:
    def __init__(self, **kwargs):
        self.id: str = kwargs.get('id')
        self.name: str = kwargs.get('name')
        self.discriminator: str = kwargs.get('discriminator')
        self.moderator_id: str = kwargs.get('moderator_id')
        self.reason: str = kwargs.get('reason')
        self.proof: str = kwargs.get('proof')
        self.is_ban_active: bool = kwargs.get('is_ban_active')
        self.can_be_appealed: bool = kwargs.get('can_be_appealed')
        self.timestamp: str = kwargs.get('timestamp')
        self.appeal_reason: Optional[str] = kwargs.get('appeal_reason')
        self.appeal_date: Optional[str] = kwargs.get('appeal_date')
        self.requested_by: str = kwargs.get('requested_by')
        self.exists: bool = kwargs.get('exists')


class BanSimple:
    def __init__(self, **kwargs):
        self.id: str = kwargs.get('id')
        self.reason: str = kwargs.get('reason')
        self.proof: str = kwargs.get('proof')
        self.moderator_id: str = kwargs.get('moderator_id')
        self.active: bool = kwargs.get('is_ban_active')


class Image:
    def __init__(self, **kwargs):
        self.url: str = kwargs.get('url')
        self.snowflake: str = kwargs.get('snowflake')
        self.nsfw: bool = kwargs.get('nsfw')
        self.tag: str = kwargs.get('tag')


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
        self.count: int = kwargs.get('ban_count')
        self.page_count: int = kwargs.get('page_count')
        self.per_page: int = kwargs.get('per_page')
        self.page: int = kwargs.get('page')
        self.on_page: int = kwargs.get('on_page')
        self.next_page: Optional[int] = kwargs.get('next_page')
        self.previous_page: Optional[int] = kwargs.get('previous_page')
        self.data: List[BanInfo] = [BanInfo(**ban) for ban in kwargs.get('data')]


class Recommendation:
    def __init__(self, data):
        youtube = data['youtube']
        spotify = data['spotify']
        spotify_album = spotify['album']
        spotify_artists = spotify['artists']

        self.name: str = data['name']

        self.youtube_id: str = youtube['id']
        self.youtube_link: str = youtube['link']
        self.youtube_title: str = youtube['title']
        self.youtube_thumbnail: str = youtube['thumbnail']

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
        self.author: str = kwargs.get('author')
        self.title: str = kwargs.get('title')
        self.image_url: str = kwargs.get('image_url')
        self.source: str = kwargs.get('source')
        self.subreddit: str = kwargs.get('subreddit')
        self.upvotes: int = kwargs.get('upvotes')
        self.downvotes: int = kwargs.get('downvotes')
        self.comments: int = kwargs.get('comments')
        self.created_at: int = kwargs.get('created_at')
        self.nsfw: bool = kwargs.get('nsfw')


class Tag:
    def __init__(self, **kwargs):
        self.name: str = kwargs.get('name')
        self.nsfw: bool = kwargs.get('nsfw')

    def __str__(self):
        return self.name


class TagCollection:
    def __init__(self, **kwargs):
        self.raw_models: List[dict] = kwargs.get('models')
        self.models: List[Tag] = [Tag(**t) for t in self.raw_models]
        self.sfw_tags: List[str] = kwargs.get('tags')
        self.nsfw_tags: List[str] = kwargs.get('nsfw_tags', [])

    def __len__(self):
        return len(self.models)

    def __dict__(self):
        return self.raw_models

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
        self.url: str = kwargs.get('url')
        self.title: str = kwargs.get('title')
        self.nsfw: bool = kwargs.get('nsfw')
        self.article_url: str = kwargs.get('article_url')
