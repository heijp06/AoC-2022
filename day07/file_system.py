from __future__ import annotations
from abc import ABC, abstractmethod


class Entry(ABC):
    def __init__(self, name: str) -> Entry:
        self.name = name

    def __repr__(self) -> None:
        return self.name

    @abstractmethod
    def get_size(self) -> int:
        pass


class Directory(Entry):
    def __init__(self, name: str, parent: Directory = None) -> None:
        super().__init__(name)
        self.entries: list[Entry] = []
        self.parent = parent or self

    def find_entry(self, name: str) -> Entry:
        return next(entry for entry in self.entries if entry.name == name)

    def get_size(self) -> int:
        return sum(entry.get_size() for entry in self.entries)


class File(Entry):
    def __init__(self, name: str, size: int) -> None:
        self.size = size
        super().__init__(name)

    def get_size(self) -> int:
        return self.size
