# -*- coding: utf-8 -*-

"""KSoft.Si API Wrapper with discord.py integration
"""

__title__ = 'ksoftapi'
__author__ = 'AndyTempel'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018-2020 AndyTempel'
__version__ = '0.2.0a'

import logging
from collections import namedtuple

from .client import Client
from .data_objects import *
from .errors import *
from .events import *

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=2, micro=0, releaselevel='alpha', serial=0)

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
