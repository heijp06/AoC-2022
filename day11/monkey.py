from __future__ import annotations
import re
from functools import partial
from typing import Callable


def parse(rows: list[str], divisor: int) -> list[Monkey]:
    monkeys: list[Monkey] = []
    for row in rows:
        line = re.findall(r"[^:, ]+", row)
        match line:
            case ['Monkey', _]:
                monkey = Monkey(divisor)
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
                monkey.modulus = int(value)
            case ['If', 'true', 'throw', 'to', 'monkey', value]:
                monkey.when_true = int(value)
            case ['If', 'false', 'throw', 'to', 'monkey', value]:
                monkey.when_false = int(value)
    return monkeys


class Monkey:
    def __init__(self, divisor: int) -> None:
        self.items: list[int] = []
        self.operation: Callable[[int], int] = int
        self.modulus = 0
        self.when_true: int = 0
        self.when_false: int = 0
        self.business = 0
        self.divisor = divisor

    def __repr__(self) -> str:
        return f"[{self.items}, %{self.modulus} ? {self.when_true} : {self.when_false}]"

    def mul(self, operand: int, item: int) -> int:
        return operand * item

    def add(self, argument: int, item: int) -> int:
        return argument + item

    def square(self, item: int) -> int:
        return item**2

    def inspect(self) -> tuple[int, int]:
        self.business += 1
        item = self.items.pop(0)
        new_item = self.operation(item) // self.divisor
        new_monkey = self.when_false if new_item % self.modulus else self.when_true
        return new_monkey, new_item
