# -*- coding: utf-8 -*-
class NoResults(Exception):
    pass


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


class NotFound(Exception):
    pass


class InvalidMethod(Exception):
    pass


class APIError(Exception):
    def __init__(self, err_msg: str = None, **data):
        self.message = data.get('message', 'No message provided')
        self.code = data.get('code', 0)
        err_msg = 'code {}: {}{}'.format(self.code, self.message, err_msg or '')

        super().__init__(err_msg)
