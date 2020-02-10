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

    # def __hash__(self):
    #     return hash('{}_{}'.format(int(self.nsfw), self.name))

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
