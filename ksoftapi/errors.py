# -*- coding: utf-8 -*-
class NoResults(Exception):
    pass


class Forbidden(Exception):
    pass


class APIError(Exception):
    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.code: int = code
        self.message: str = message
