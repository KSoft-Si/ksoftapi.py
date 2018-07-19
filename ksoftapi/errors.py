# -*- coding: utf-8 -*-


class RequireFormatting(Exception):
    pass


class MissingRequiredArguments(Exception):
    pass


class WeirdResponse(Exception):
    pass


class SpecifyClient(Exception):
    pass


class Forbidden(Exception):
    pass


class DiscordPyNotInstalled(Exception):
    pass


class NotFound(Exception):
    pass


class InvalidMethod(Exception):
    pass


class APIError(Exception):
    def __init__(self, err_msg: str=None, **data):
        self.message = data.get("message", "No message provided")
        self.code = data.get("code", 0)
        if err_msg is not None:
            err_msg = " | Additional info: {}".format(err_msg)
        err_msg = "code {}: {}{}".format(self.code, self.message, err_msg)
        super().__init__(err_msg)
