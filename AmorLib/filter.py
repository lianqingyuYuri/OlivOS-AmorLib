# -*- encoding: utf-8 -*-
"""
@File      :    AmorLib/filter.py
@Author    :    lianqingyuYuri恋倾雨
@Contact   :    xinghu2408@foxmail.com
@License   :    AGPLv3
@Copyright :    (C) 2026 AmorLib
@Desc      :    通用过滤器与注册器：以函数为键挂载过滤器链，按 AND 短路逻辑匹配事件; 事件类型泛型化(EventT), 不绑定具体事件对象。
"""

from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Generic, TypeVar

EventT = TypeVar("EventT")


class HandlerFilter(ABC, Generic[EventT]):
    """过滤器基类，返回 True 表示放行。"""

    @abstractmethod
    def filter(self, event: EventT) -> bool:
        pass


@dataclass
class Entry(Generic[EventT]):
    """一条记录：处理函数 + 过滤器链。"""

    func: Callable
    filters: list[HandlerFilter[EventT]] = field(default_factory=list)

    @property
    def name(self) -> str:
        return self.func.__name__


class Registry(Generic[EventT]):
    """通用注册器：以函数对象为键，为任意事件类型挂载过滤器链。"""

    def __init__(self) -> None:
        self._entries: dict[Callable, Entry[EventT]] = {}

    def get_or_create(self, func: Callable) -> Entry[EventT]:
        """获取或创建条目"""
        entry = self._entries.get(func)
        if entry is None:
            entry = Entry(func=func)
            self._entries[func] = entry
        return entry

    def attach(self, func: Callable, flt: HandlerFilter[EventT]) -> Entry[EventT]:
        """登记一个过滤器"""
        entry = self.get_or_create(func)
        if flt not in entry.filters:
            entry.filters.append(flt)
        return entry

    def pass_filters(self, entry: Entry[EventT], event: EventT) -> bool:
        """对某条目的过滤器链求值（AND，短路）。"""
        return all(f.filter(event) for f in entry.filters)

    def match_handlers(self, event: EventT) -> list[Entry[EventT]]:
        """返回所有过滤器链通过的条目。"""
        return [e for e in self._entries.values() if self.pass_filters(e, event)]

    def entries(self) -> list[Entry[EventT]]:
        """返回所有登记的条目"""
        return list(self._entries.values())

    def clear(self) -> None:
        """清除所有登记的条目"""
        self._entries.clear()
