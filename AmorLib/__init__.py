# -*- encoding: utf-8 -*-
"""
@File      :    AmorLib/__init__.py
@Author    :    lianqingyuYuri恋倾雨
@Contact   :    None
@License   :    AGPLv3
@Copyright :    (C) 2026 AmorLib
@Desc      :    None
"""

__version__ = "2.0.0"

STRING_ROW = list[str] | tuple[str, ...]
import platform

is_windows = platform.system() == "Windows"

from .base import Registerable
from .cfg import IniConfig
from .custom import (
    MsgManager,
    releaseDir,
    initCustom,
    readCustom,
    readCustomByBotHash,
    saveCustom,
    saveCustomByBotHash,
    loadCustomInto,
    has_NativeGUI,
)
from .db import DataBase, execute
from .router import UniqueRouter, FsmRouter, PriorityRouter
