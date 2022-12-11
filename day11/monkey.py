from __future__ import annotations
import re
from functools import partial
from typing import Callable, Optional


@staticmethod
def parse(rows: list[str]) -> list[Monkey]:
    monkeys: list[Monkey] = []
    for row in rows:
        line = re.findall(r"[^:, ]+", row)
        match line:
            case ['Monkey', *_]:
                monkey = Monkey()
                monkeys.append(monkey)
            case ['Starting', 'items', *items]:
                monkey.items = list(map(int, items))
            case ['Operation', 'new', '=', 'old', *operation]:
                match operation:
                    case ['*', 'old']:
                        monkey.operation = monkey.square
                    case ['*', value]:
                        monkey.operation = partial(monkey.mul, int(value))
                    case ['+', value]:
                        monkey.operation = partial(monkey.add, int(value))
            case ['Test', 'divisible', 'by', value]:
                monkey.divisor = int(value)
            case ['If', 'true', 'throw', 'to', 'monkey', value]:
                monkey.when_true = int(value)
            case ['If', 'false', 'throw', 'to', 'monkey', value]:
                monkey.when_false = int(value)
    return monkeys


class Monkey:
    def __init__(self) -> None:
        self.items: list[int] = []
        self.operation: Optional[Callable[[int], int]] = None
        self.divisor = 0
        self.when_true: Optional[int] = None
        self.when_false: Optional[int] = None
        self.business = 0

    def __repr__(self) -> str:
        return f"[{self.items}, %{self.divisor} ? {self.when_true} : {self.when_false}]"

    def mul(self, argument: int, item: int) -> int:
        return argument * item

    def add(self, argument: int, item: int) -> int:
        return argument + item

    def square(self, item: int) -> int:
        return item**2

    def inspect(self) -> tuple[int, int]:
        self.business += 1
        item = self.items.pop(0)
        new_item = self.operation(item) // 3
        new_monkey = self.when_false if new_item % self.divisor else self.when_true
        return new_monkey, new_item