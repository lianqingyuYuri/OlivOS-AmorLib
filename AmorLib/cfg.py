# -*- encoding: utf-8 -*-
"""
@File      :    AmorLib/cfg.py
@Author    :    lianqingyuYuri恋倾雨
@Contact   :    xinghu2408@foxmail.com
@License   :    AGPLv3
@Copyright :    (C) 2026 MammonRoulette
@Desc      :    None
"""

import configparser
from typing import TypeVar, Union

T = TypeVar("T")


class IniConfig:
    def __init__(self, filename: str, encoding: str = "utf-8"):
        self.filename = filename
        self.encoding = encoding
        self.parser = configparser.ConfigParser()

    def __enter__(self):
        read_ok = self.parser.read(self.filename, encoding=self.encoding)
        if not read_ok:
            raise FileNotFoundError(f"无法读取配置文件: {self.filename}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get(self, section: str, key: str, fallback: T = None) -> Union[str, T]:
        """
        获取指定配置项的值。
        :param section: 节名
        :param key: 键名
        :param fallback: 如果键不存在时返回的默认值
        :return: 配置值（字符串），若不存在且未提供 fallback 则返回 None
        """
        return self.parser.get(section, key, fallback=fallback)

    def sections(self):
        """返回所有节名列表。"""
        return self.parser.sections()

    def items(self, section: str):
        """返回指定节的所有键值对。"""
        return self.parser.items(section)

    def getint(self, section: str, key: str, fallback: int | None = None) -> int | None:
        return self.parser.getint(section, key, fallback=fallback)

    def getfloat(
        self, section: str, key: str, fallback: float | None = None
    ) -> float | None:
        return self.parser.getfloat(section, key, fallback=fallback)

    def getboolean(
        self, section: str, key: str, fallback: bool | None = None
    ) -> bool | None:
        return self.parser.getboolean(section, key, fallback=fallback)
