from typing import Dict, List, Optional


class BanInfo:
    def __init__(self, data: dict):
        self.id: str = data['id']
        self.name: str = data['name']
        self.discriminator: str = data['discriminator']
        self.moderator_id: str = data['moderator_id']
        self.reason: str = data['reason']
        self.proof: str = data['proof']
        self.is_ban_active: bool = data['is_ban_active']
        self.can_be_appealed: bool = data['can_be_appealed']
        self.timestamp: str = data['timestamp']
        self.appeal_reason: Optional[str] = data['appeal_reason']
        self.appeal_date: Optional[str] = data['appeal_date']
        self.requested_by: str = data['requested_by']
        self.exists: bool = data['exists']
        self.raw: dict = data


class BanSimple:
    def __init__(self, data: dict):
        self.id: str = data['id']
        self.reason: str = data['reason']
        self.proof: str = data['proof']
        self.moderator_id: str = data['moderator_id']
        self.active: bool = data['is_ban_active']
        self.raw: dict = data


class Image:
    def __init__(self, data: dict):
        self.url: str = data['url']
        self.snowflake: str = data['snowflake']
        self.nsfw: bool = data['nsfw']
        self.tag: str = data['tag']
        self.raw: dict = data


class Location:
    def __init__(self, data: dict):
        self.address: str = data['address']
        self.lat: float = data['lat']
        self.lon: float = data['lon']
        self.bounding_box: List[str] = data['bounding_box']
        self.type: List[str] = data['type']
        self.map: Optional[str] = data.get('map')
        self.raw: dict = data


class LyricResult:
    def __init__(self, data: dict):
        self.artist: str = data['artist']
        self.artist_id: int = data['artist_id']
        self.album: str = data['album']
        self.album_ids: List[str] = data['album_ids'].split(',')
        self.album_year: List[str] = data['album_year'].split(',')
        self.name: str = data['name']
        self.lyrics: str = data['lyrics']
        self.search_str: str = data['search_str']
        self.album_art: str = data['album_art']
        self.popularity: int = data['popularity']
        self.id: str = data['id']
        self.search_score: float = data['search_score']
        self.url: str = data['url']
        self.raw: dict = data


class PaginatorListing:
    def __init__(self, data: dict):
        self.count: int = data['ban_count']
        self.page_count: int = data['page_count']
        self.per_page: int = data['per_page']
        self.page: int = data['page']
        self.on_page: int = data['on_page']
        self.next_page: Optional[int] = data['next_page']
        self.previous_page: Optional[int] = data['previous_page']
        self.data: List[BanInfo] = [BanInfo(ban) for ban in data['data']]
        self.raw: dict = data


class Recommendation:
    def __init__(self, data: dict):
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
        self.raw: dict = data


class RedditImage:
    def __init__(self, data: dict):
        self.author: str = data.get('author')
        self.title: str = data.get('title')
        self.image_url: str = data.get('image_url')
        self.source: str = data.get('source')
        self.subreddit: str = data.get('subreddit')
        self.upvotes: int = data.get('upvotes')
        self.downvotes: int = data.get('downvotes')
        self.comments: int = data.get('comments')
        self.created_at: int = data.get('created_at')
        self.nsfw: bool = data.get('nsfw')
        self.raw: dict = data


class Tag:
    def __init__(self, data: dict):
        self.name: str = data.get('name')
        self.nsfw: bool = data.get('nsfw')
        self.raw: dict = data

    def __str__(self):
        return self.name


class TagCollection:
    def __init__(self, data: dict):
        self.raw_models: List[dict] = data.get('models')
        self.models: List[Tag] = [Tag(t) for t in self.raw_models]
        self.sfw_tags: List[str] = data.get('tags')
        self.nsfw_tags: List[str] = data.get('nsfw_tags', [])
        self.raw: dict = data

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
    def __init__(self, data: dict):
        self.url: str = data.get('url')
        self.title: str = data.get('title')
        self.nsfw: bool = data.get('nsfw')
        self.article_url: str = data.get('article_url')
        self.raw: dict = data


class IPInfo:
    def __init__(self, data: dict):
        self.city: str = data.get('city')
        self.continent_code: str = data.get('continent_code')
        self.continent_name: str = data.get('continent_name')
        self.country_code: str = data.get('country_code')
        self.country_name: str = data.get('country_name')
        self.dma_code: str = data.get('dma_code')
        self.latitude: float = data.get('latitude')
        self.longitude: float = data.get('longitude')
        self.postal_code: str = data.get('postal_code')
        self.region: str = data.get('region')
        self.timezone: str = data.get('time_zone')
        self.apis: Dict[str, str] = data.get('apis')
        self.raw: dict = data


class Currency:
    def __init__(self, data: dict):
        self.value: float = data.get('value')
        self.pretty: str = data.get('pretty')
