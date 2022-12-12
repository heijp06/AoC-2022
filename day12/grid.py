from collections import namedtuple
from itertools import product


Position = namedtuple("Position", "row,col")


class Grid:
    def __init__(self, rows: list[str]) -> None:
        self.height = len(rows)
        self.width = len(rows[0])
        self._grid: list[list[int]] = []
        for row, _ in enumerate(rows):
            line: list[int] = []
            self._grid.append(line)
            for column, _ in enumerate(rows[0]):
                letter = rows[row][column]
                if letter == 'S':
                    line.append(0)
                    self.start = Position(row, column)
                elif letter == 'E':
                    line.append(25)
                    self.end = Position(row, column)
                else:
                    line.append(ord(letter) - ord('a'))

    def __getitem__(self, position: Position) -> int:
        return self._grid[position.row][position.col]

    def get_positions(self) -> list[Position]:
        return [Position(row, col) for row, col in product(range(self.height), range(self.width))]

    def on_grid(self, position: Position) -> bool:
        return (position.row >= 0 and position.row < self.height and
                position.col >= 0 and position.col < self.width)
