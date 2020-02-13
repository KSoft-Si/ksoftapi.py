class BanUpdateEvent:
    def __init__(self, data: dict):
        self.id: str = data['id']
        self.moderator_id: str = data['moderator_id']
        self.reason: str = data['reason']
        self.proof: str = data['proof']
        self.active: bool = data['active']
