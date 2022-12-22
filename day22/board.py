from __future__ import annotations
import re
from typing import Any, NamedTuple


def parse(rows: list[str]) -> Board:
    width = max(len(row) for row in rows)
    board_rows = [" " * (width + 2)]
    for index in range(len(rows) - 2):
        row = rows[index]
        board_rows.append(f" {row}" + " " * (width - len(row) + 1))
    board_rows += [" " * (width + 2)]
    commands = []
    parse_int = True
    for field in re.findall(r"[A-Z]+|\d+", rows[-1]):
        commands.append(int(field) if parse_int else field)
        parse_int = not parse_int
    return Board(board_rows, commands)


class Position(NamedTuple):
    row: int
    column: int

    def __add__(self, other: Position) -> Position:
        return Position(self.row + other.row, self.column + other.column)

    def __mod__(self, other: Position) -> Position:
        return Position(self.row % other.row, self.column % other.column)


class Board:
    def __init__(self, rows: list[str], commands: list[Any]) -> None:
        self.rows = rows
        self.commands = commands
        self.position = Position(1, rows[1].index("."))
        self.direction = Position(0, 1)
        self.width = len(rows[0])
        self.height = len(rows)

    def __getitem__(self, position: Position) -> str:
        return self.rows[position.row][position.column]

    def go(self) -> None:
        for command in self.commands:
            if isinstance(command, int):
                self.move(command)
            elif command == "L":
                self.left()
            elif command == "R":
                self.right()
            else:
                raise ValueError(f"Unexpected command: {command}.")

    def move(self, steps: int) -> None:
        for _ in range(steps):
            new_position = self.position + self.direction
            new_position %= Position(self.height, self.width)
            while self[new_position] == ' ':
                new_position += self.direction
                new_position %= Position(self.height, self.width)
            if self[new_position] == "#":
                return
            self.position = new_position
        return

    def right(self) -> None:
        self.direction = Position(self.direction.column, -self.direction.row)

    def left(self) -> None:
        self.direction = Position(-self.direction.column, self.direction.row)
    
    def password(self) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return 1000 * self.position.row + 4 * self.position.column + directions.index(self.direction)
