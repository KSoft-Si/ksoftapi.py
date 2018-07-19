class BanEvent:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get("id")
        self.moderator_id = kwargs.get("mod")
        self.reason = kwargs.get("reason")
        self.proof = kwargs.get("proof")


class UnBanEvent:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get("id")
        self.moderator_id = kwargs.get("mod")
        self.reason = kwargs.get("reason")
        self.proof = kwargs.get("proof")
