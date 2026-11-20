# -*- encoding: utf-8 -*-
"""
@File      :    AmorLib/__init__.py
@Author    :    lianqingyuYuri恋倾雨
@Contact   :    None
@License   :    AGPLv3
@Copyright :    (C) 2026 AmorLib
@Desc      :    None
"""

__version__ = "2.1.0"

STRING_ROW = list[str] | tuple[str, ...]
import platform

is_windows = platform.system() == "Windows"

from .base import Registerable
from .cfg import IniConfig
from .custom import (
    has_NativeGUI,
    initCustom,
    loadCustomInto,
    readCustom,
    readCustomByBotHash,
    releaseDir,
    saveCustom,
    saveCustomByBotHash,
)
from .db import DataBase, execute
from .filter import Entry, HandlerFilter, Registry
from .msg import MsgManager
from .router import FsmRouter, PriorityRouter, UniqueRouter
