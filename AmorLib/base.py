# -*- encoding: utf-8 -*-
"""
@File      :    AmorLib/base.py
@Author    :    lianqingyuYuri恋倾雨
@Contact   :    xinghu2408@foxmail.com
@License   :    AGPLv3
@Copyright :    (C) 2026 MammonRoulette
@Desc      :    None
"""


class Registerable:
    _register = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        name = getattr(cls, "name", None)
        if name:
            cls._register[name] = cls

    @classmethod
    def get(cls, name):
        return cls._register.get(name, lambda: None)

    @classmethod
    def list(cls):
        return list(cls._register.keys())
