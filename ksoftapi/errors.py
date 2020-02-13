# -*- coding: utf-8 -*-
class NoResults(Exception):
    pass


class Forbidden(Exception):
    pass


class APIError(Exception):
    def __init__(self, data: dict, err_msg: str = None):
        self.message: str = data.get('message', 'No message provided')
        self.code: int = data.get('code', 0)
        err_msg = 'code {}: {}{}'.format(self.code, self.message, err_msg or '')

        super().__init__(err_msg)
