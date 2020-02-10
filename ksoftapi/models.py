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
