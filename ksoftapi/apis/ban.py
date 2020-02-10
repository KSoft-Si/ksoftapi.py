class Ban:
    def __init__(self, client):
        self._client = client

    async def __aiter__(self):
        ...

    async def add(self, user_id: int, reason: str, proof: str,
                  mod=None, user_name=None, user_discriminator=None, appeal_possible=None):
        ...

    async def check(self, user_id: int) -> bool:
        ...

    async def info(self, user_id: int):
        ...

    async def remove(self, user_id: int):
        ...

    # async def bans_add(self, user_id: int, reason: str, proof: str, **kwargs):
    #     arg_params = ["mod", "user_name", "user_discriminator", "appeal_possible"]
    #     data = {
    #         "user": user_id,
    #         "reason": reason,
    #         "proof": proof
    #     }
    #     for arg, val in kwargs.items():
    #         if arg in arg_params:
    #             data.update({arg: val})
    #         else:
    #             raise ValueError(f"unknown parameter: {arg}")
    #     r = await self.http.request(Route.bans("POST", "/add"), data=data)
    #     if r.get("success", False) is True:
    #         return True
    #     else:
    #         raise APIError(**r)

    # async def bans_check(self, user_id: int) -> bool:
    #     r = await self.http.request(Route.bans("GET", "/check"), params={"user": user_id})
    #     if r.get("is_banned", None) is not None:
    #         return r['is_banned']
    #     else:
    #         raise APIError(**r)

    # async def bans_info(self, user_id: int) -> Ban:
    #     r = await self.http.request(Route.bans("GET", "/info"), params={"user": user_id})
    #     if r.get("is_ban_active", None) is not None:
    #         return Ban(**r)
    #     else:
    #         raise APIError(**r)

    # async def bans_remove(self, user_id: int) -> bool:
    #     r = await self.http.request(Route.bans("DELETE", "/remove"), params={"user": user_id})
    #     if r.get("done", None) is not None:
    #         return True
    #     else:
    #         raise APIError(**r)

    # def ban_get_list_iterator(self):
    #     return BanIterator(self, Route.bans("GET", "/list"))
