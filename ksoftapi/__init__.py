# -*- coding: utf-8 -*-

"""
KSoft.Si API Wrapper with discord.py integration
"""

__title__ = 'ksoftapi'
__author__ = 'AndyTempel'
__license__ = 'GNU'
__copyright__ = 'Copyright 2018-2020 AndyTempel'
__version__ = '0.3.1a'

import logging
from collections import namedtuple

from .client import Client  # noqa: F401
from .errors import APIError, Forbidden, NoResults  # noqa: F401
from .events import BanUpdateEvent  # noqa: F401

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=3, micro=1, releaselevel='alpha', serial=0)

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
