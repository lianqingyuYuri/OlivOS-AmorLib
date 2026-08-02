# -*- encoding: utf-8 -*-
"""
@File      :    AmorLib/__init__.py
@Author    :    lianqingyuYuri恋倾雨
@Contact   :    None
@License   :    AGPLv3
@Copyright :    (C) 2026 AmorLib
@Desc      :    None
"""

STRING_ROW = list[str] | tuple[str, ...]

from .cfg import IniConfig
from .db import DataBase, execute
from .msgRouter import UniqueRouter, FsmRouter, PriorityRouter
from .msgCustomManager import MsgManager, init_msgCustom, has_NativeGUI
