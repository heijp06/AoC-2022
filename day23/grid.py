from __future__ import annotations
from collections import defaultdict
from functools import lru_cache
from itertools import starmap
from typing import Optional


def parse(rows: list[str]) -> Grid:
    elves: list[Position] = []
    for row in range(len(rows)):
        elves.extend(
            Position(row, column)
            for column in range(len(rows[0]))
            if rows[row][column] == "#"
        )
    return Grid(elves)


class Position:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column

    def _key(self) -> tuple[int, int]:
        return (self.row, self.column)

    def __repr__(self) -> str:
        return repr(self._key())

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Position) and self._key() == other._key()

    def __hash__(self) -> int:
        return hash(self._key())

    def __add__(self, other) -> Position:
        return Position(self.row + other.row, self.column + other.column)


class Grid:
    def __init__(self, elves: list[Position]) -> None:
        self.elves = frozenset(elves)
        self.rules = (
            (Position(-1, 0), Position(-1, -1), Position(-1, 1)),
            (Position(1, 0), Position(1, -1), Position(1, 1)),
            (Position(0, -1), Position(-1, -1), Position(1, -1)),
            (Position(0, 1), Position(-1, 1), Position(1, 1))
        )

    def _key(self) -> tuple[frozenset[Position], tuple[tuple[Position, Position, Position], ...]]:
        return (self.elves, tuple(self.rules))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Grid) and self._key() == other._key()

    def __hash__(self) -> int:
        return hash(self._key())

    def do_round(self) -> bool:
        directions: dict[Position, int] = defaultdict(int)
        for elf in self.elves:
            direction = self.get_direction(elf)
            if direction is not None:
                directions[direction] += 1
        new_elves: set[Position] = set()
        for elf in self.elves:
            direction = self.get_direction(elf)
            if direction is not None and directions[direction] == 1:
                new_elves.add(direction)
                continue
            new_elves.add(elf)
        self.rules = self.rules[1:] + self.rules[:1]
        if self.elves == new_elves:
            return True
        self.elves = frozenset(new_elves)
        return False

    def move(self, elf: Position) -> bool:
        return any(
            elf + position in self.elves
            for position in starmap(
                Position,
                (
                    (x, y)
                    for x in range(-1, 2)
                    for y in range(-1, 2)
                    if (x, y) != (0, 0)
                )
            )
        )

    def get_bounds(self) -> tuple[Position, Position]:
        min_row = min(elf.row for elf in self.elves)
        max_row = max(elf.row for elf in self.elves)
        min_column = min(elf.column for elf in self.elves)
        max_column = max(elf.column for elf in self.elves)
        return (Position(min_row, min_column), Position(max_row, max_column))

    def get_width(self) -> int:
        top_left, bottom_right = self.get_bounds()
        return bottom_right.column - top_left.column + 1

    def get_height(self) -> int:
        top_left, bottom_right = self.get_bounds()
        return bottom_right.row - top_left.row + 1

    def dump(self):
        top_left, bottom_right = self.get_bounds()
        for row in range(top_left.row, bottom_right.row + 1):
            for column in range(top_left.column, bottom_right.column + 1):
                if Position(row, column) in self.elves:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()

    @lru_cache(maxsize=1000000)
    def get_direction(self, elf: Position) -> Optional[Position]:
        if not self.move(elf):
            return None
        for rule in self.rules:
            new_position = self.get_new_position(elf, rule)
            if new_position is not None:
                return new_position
        return None

    def get_new_position(
            self,
            elf: Position,
            directions: tuple[Position, Position, Position]) -> Optional[Position]:
        new_positions = {elf + direction for direction in directions}
        return (
            None
            if self.elves & new_positions
            else Position(elf.row, elf.column) + directions[0]
        )
