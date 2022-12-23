from __future__ import annotations
from collections import defaultdict
from itertools import starmap
from typing import NamedTuple, Optional


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
        self.elves = set(elves)
        self.rules = ["N", "S", "W", "E"]

    def do_round(self) -> bool:
        directions: dict[Position, int] = defaultdict(int)
        for elve in self.elves:
            if self.move(elve):
                direction = self.get_direction(elve)
                if direction is not None:
                    directions[direction] += 1
        new_elves: set[Position] = set()
        for elve in self.elves:
            if self.move(elve):
                direction = self.get_direction(elve)
                if direction is not None and directions[direction] == 1:
                    new_elves.add(direction)
                    continue
            new_elves.add(elve)
        self.rules = self.rules[1:] + self.rules[:1]
        if self.elves == new_elves:
            return True
        self.elves = new_elves
        return False

    def move(self, elve: Position) -> bool:
        return any(
            elve + position in self.elves
            for position in starmap(
                Position,
                iter(
                    [
                        (x, y)
                        for x in range(-1, 2)
                        for y in range(-1, 2)
                        if (x, y) != (0, 0)
                    ]
                ),
            )
        )

    def dump(self):
        min_row = min(elve.row for elve in self.elves)
        max_row = max(elve.row for elve in self.elves)
        min_column = min(elve.column for elve in self.elves)
        max_column = max(elve.column for elve in self.elves)
        for row in range(min_row, max_row + 1):
            for column in range(min_column, max_column + 1):
                if Position(row, column) in self.elves:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()

    def get_direction(self, elve: Position) -> Optional[Position]:
        for position in self.rules:
            match position:
                case "N":
                    new_positions = {
                        elve + direction
                        for direction in [
                            Position(-1, 0),
                            Position(-1, -1),
                            Position(-1, 1),
                        ]
                    }
                    if not self.elves & new_positions:
                        return Position(elve.row - 1, elve.column)
                case "S":
                    new_positions = {
                        elve + direction
                        for direction in [
                            Position(1, 0),
                            Position(1, -1),
                            Position(1, 1),
                        ]
                    }
                    if not self.elves & new_positions:
                        return Position(elve.row + 1, elve.column)
                case "W":
                    new_positions = {
                        elve + direction
                        for direction in [
                            Position(0, -1),
                            Position(-1, -1),
                            Position(1, -1),
                        ]
                    }
                    if not self.elves & new_positions:
                        return Position(elve.row, elve.column - 1)
                case "E":
                    new_positions = {
                        elve + direction
                        for direction in [
                            Position(0, 1),
                            Position(-1, 1),
                            Position(1, 1),
                        ]
                    }
                    if not self.elves & new_positions:
                        return Position(elve.row, elve.column + 1)
        return None
