from __future__ import annotations
import re
from typing import Any, Callable, NamedTuple


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
    return Board(board_rows, commands, get_face(width))


def get_face(width: int) -> Face:
    return get_face_example() if width < 20 else get_face_input()


def get_face_example() -> Face:
    face1 = Face(1, Position(1, 9), Position(4, 12))
    face2 = Face(2, Position(5, 1), Position(8, 4))
    face3 = Face(3, Position(5, 5), Position(8, 8))
    face4 = Face(4, Position(5, 9), Position(8, 12))
    face5 = Face(5, Position(9, 9), Position(12, 12))
    face6 = Face(6, Position(9, 13), (Position(12, 16)))

    face1.right = lambda p: (face6, Position(13 - p.row, 16), Position(0, -1))
    face1.down = lambda p: (face4, Position(5, p.column), Position(1, 0))
    face1.left = lambda p: (face3, Position(5, 4 + p.row), Position(1, 0))
    face1.up = lambda p: (face2, Position(5, 13 - p.column), Position(1, 0))

    face2.right = lambda p: (face3, Position(p.row, 5), Position(0, 1))
    face2.down = lambda p: (face5, Position(
        16, 13 - p.column), Position(-1, 0))
    face2.left = lambda p: (face6, Position(
        16, 12 + p.column), Position(-1, 0))
    face2.up = lambda p: (face1, Position(1, 13 - p.column), Position(1, 0))

    face3.right = lambda p: (face4, Position(p.row, 9), Position(0, 1))
    face3.down = lambda p: (face5, Position(17 - p.column, 9), Position(0, 1))
    face3.left = lambda p: (face2, Position(p.row, 4), Position(0, -1))
    face3.up = lambda p: (face1, Position(p.column - 4, 9), Position(0, 1))

    face4.right = lambda p: (face6, Position(9, 21 - p.row), Position(1, 0))
    face4.down = lambda p: (face5, Position(9, p.column), Position(1, 0))
    face4.left = lambda p: (face3, Position(p.row, 8), Position(0, -1))
    face4.up = lambda p: (face1, Position(4, p.column), Position(-1, 0))

    face5.right = lambda p: (face6, Position(p.row, 13), Position(0, 1))
    face5.down = lambda p: (face2, Position(8, 13 - p.column), Position(-1, 0))
    face5.left = lambda p: (face3, Position(8, 17 - p.row), Position(-1, 0))
    face5.up = lambda p: (face4, Position(8, p.column), Position(-1, 0))

    face6.right = lambda p: (face1, Position(13 - p.row, 12), Position(0, -1))
    face6.down = lambda p: (face2, Position(21 - p.column, 1), Position(0, 1))
    face6.left = lambda p: (face5, Position(p.row, 12), Position(0, -1))
    face6.up = lambda p: (face4, Position(21 - p.column, 12), Position(0, -1))

    return face1


def get_face_input() -> Face:
    face1 = Face(1, Position(1, 51), Position(50, 100))
    face2 = Face(2, Position(1, 101), Position(50, 150))
    face3 = Face(3, Position(51, 51), Position(100, 100))
    face4 = Face(4, Position(101, 1), Position(150, 50))
    face5 = Face(5, Position(101, 51), Position(150, 100))
    face6 = Face(6, Position(151, 1), Position(200, 50))

    face1.right = lambda p: (face2, Position(p.row, 101), Position(0, 1))
    face1.down = lambda p: (face3, Position(51, p.column), Position(1, 0))
    face1.left = lambda p: (face4, Position(151 - p.row, 1), Position(0, 1))
    face1.up = lambda p: (face6, Position(100 + p.column, 1), Position(0, 1))

    face2.right = lambda p: (face5, Position(
        151 - p.row, 100), Position(0, -1))
    face2.down = lambda p: (face3, Position(
        p.column - 50, 100), Position(0, -1))
    face2.left = lambda p: (face1, Position(p.row, 100), Position(0, -1))
    face2.up = lambda p: (face6, Position(
        200, p.column - 100), Position(-1, 0))

    face3.right = lambda p: (face2, Position(50, p.row + 50), Position(-1, 0))
    face3.down = lambda p: (face5, Position(101, p.column), Position(1, 0))
    face3.left = lambda p: (face4, Position(101, p.row - 50), Position(1, 0))
    face3.up = lambda p: (face1, Position(50, p.column), Position(-1, 0))

    face4.right = lambda p: (face5, Position(p.row, 51), Position(0, 1))
    face4.down = lambda p: (face6, Position(151, p.column), Position(1, 0))
    face4.left = lambda p: (face1, Position(151 - p.row, 51), Position(0, 1))
    face4.up = lambda p: (face3, Position(50 + p.column, 51), Position(0, 1))

    face5.right = lambda p: (face2, Position(
        151 - p.row, 150), Position(0, -1))
    face5.down = lambda p: (face6, Position(
        p.column + 100, 50), Position(0, -1))
    face5.left = lambda p: (face4, Position(p.row, 50), Position(0, -1))
    face5.up = lambda p: (face3, Position(100, p.column), Position(-1, 0))

    face6.right = lambda p: (face5, Position(
        150, p.row - 100), Position(-1, 0))
    face6.down = lambda p: (face2, Position(1, p.column + 100), Position(1, 0))
    face6.left = lambda p: (face1, Position(1, p.row - 100), Position(1, 0))
    face6.up = lambda p: (face4, Position(150, p.column), Position(-1, 0))

    return face1


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

    def __add__(self, other: Position) -> Position:
        return Position(self.row + other.row, self.column + other.column)

    def __mod__(self, other: Position) -> Position:
        return Position(self.row % other.row, self.column % other.column)


class Face:
    def __init__(self, name: int, start: Position, end: Position) -> None:
        self.name = name
        self.start = start
        self.end = end
        self.right: Callable[[Position], tuple[Face, Position, Position]]
        self.down: Callable[[Position], tuple[Face, Position, Position]]
        self.left: Callable[[Position], tuple[Face, Position, Position]]
        self.up: Callable[[Position], tuple[Face, Position, Position]]

    def __repr__(self) -> str:
        return f"{self.name}"

    def move_off_edge(self, position: Position, direction: Position) -> tuple[Face, Position, Position]:
        if direction == (0, 1) and position.column == self.end.column:
            return self.right(position)
        elif direction == (1, 0) and position.row == self.end.row:
            return self.down(position)
        elif direction == (0, -1) and position.column == self.start.column:
            return self.left(position)
        elif direction == (-1, 0) and position.row == self.start.row:
            return self.up(position)
        raise ValueError(
            f"Cannot move off edge on face {self.name} at {position} in direction {direction}")


class Board:
    def __init__(self, rows: list[str], commands: list[Any], face: Face) -> None:
        self.rows = rows
        self.commands = commands
        self.position = Position(1, rows[1].index("."))
        self.direction = Position(0, 1)
        self.width = len(rows[0])
        self.height = len(rows)
        self.face = face

    def __getitem__(self, position: Position) -> str:
        return self.rows[position.row][position.column]

    def go(self, part: int) -> None:
        for command in self.commands:
            if isinstance(command, int):
                self.move(command) if part == 1 else self.cube_move(command)
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

    def cube_move(self, steps: int) -> None:
        for _ in range(steps):
            if self.direction == Position(0, 1) and self.position.column == self.face.end.column:
                new_face, new_position, new_direction = self.face.right(
                    self.position)
            elif self.direction == Position(1, 0) and self.position.row == self.face.end.row:
                new_face, new_position, new_direction = self.face.down(
                    self.position)
            elif self.direction == Position(0, -1) and self.position.column == self.face.start.column:
                new_face, new_position, new_direction = self.face.left(
                    self.position)
            elif self.direction == Position(-1, 0) and self.position.row == self.face.start.row:
                new_face, new_position, new_direction = self.face.up(
                    self.position)
            else:
                new_face = self.face
                new_position = self.position + self.direction
                new_direction = self.direction
            if self[new_position] == ' ':
                raise ValueError("Fell of the cube.")
            if self[new_position] == "#":
                return
            self.face = new_face
            self.position = new_position
            self.direction = new_direction

    def right(self) -> None:
        self.direction = Position(self.direction.column, -self.direction.row)

    def left(self) -> None:
        self.direction = Position(-self.direction.column, self.direction.row)

    def password(self) -> int:
        directions = [Position(0, 1), Position(1, 0), Position(0, -1), Position(-1, 0)]
        return 1000 * self.position.row + 4 * self.position.column + directions.index(self.direction)
