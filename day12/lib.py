import itertools
from collections import namedtuple


Grid = list[list[int]]
Position = namedtuple("Position", "row,col")


def part1(rows: list[str]) -> int:
    start, end, grid = parse(rows)
    return find([start], end, grid)


def find(starts, end, grid):
    height = len(grid)
    width = len(grid[0])
    if end in starts:
        return 0
    positions = starts
    seen = set(starts)
    step = 1
    while positions:
        new_positions: list[Position] = []
        for pos in positions:
            for delta in [Position(0, 1), Position(0, -1), Position(1, 0), Position(-1, 0)]:
                new_pos = Position(pos.row + delta.row, pos.col + delta.col)
                if new_pos.row < 0 or new_pos.row >= height or new_pos.col < 0 or new_pos.col >= width:
                    continue
                if new_pos in seen:
                    continue
                if grid[new_pos.row][new_pos.col] - grid[pos.row][pos.col] > 1:
                    continue
                if new_pos == end:
                    return step
                new_positions.append(new_pos)
                seen.add(new_pos)
        step += 1
        positions = new_positions


def part2(rows: list[str]) -> int:
    _, end, grid = parse(rows)
    height = len(grid)
    width = len(grid[0])
    starts = [Position(row, col) for row, col in itertools.product(
        range(height), range(width)) if not grid[row][col]]
    return find(starts, end, grid)
    #         length = find(Position(row, col), end, grid)
    #         if length < best:
    #             best = length
    # return best


def parse(rows: list[str]) -> tuple[Position, Position, Grid]:
    grid: Grid = []
    start = Position(-1, -1)
    end = Position(-1, -1)
    for row in range(len(rows)):
        line: list[int] = []
        grid.append(line)
        for column in range(len(rows[0])):
            letter = rows[row][column]
            if letter == 'S':
                line.append(0)
                start = Position(row, column)
            elif letter == 'E':
                line.append(25)
                end = Position(row, column)
            else:
                line.append(ord(letter) - ord('a'))
    return start, end, grid
