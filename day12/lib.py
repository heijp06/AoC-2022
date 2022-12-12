from typing import Optional
from grid import Grid, Position


def part1(rows: list[str]) -> Optional[int]:
    grid = Grid(rows)
    return find([grid.start], grid)


def part2(rows: list[str]) -> Optional[int]:
    grid = Grid(rows)
    starts = [position for position in grid.get_positions()
              if not grid[position]]
    return find(starts, grid)


def find(starts: list[Position], grid: Grid) -> Optional[int]:
    if grid.end in starts:
        return 0
    positions = starts
    seen = set(starts)
    step = 1
    while positions:
        new_positions: list[Position] = []
        for pos in positions:
            for delta in [Position(0, 1), Position(0, -1), Position(1, 0), Position(-1, 0)]:
                new_pos = Position(pos.row + delta.row, pos.col + delta.col)
                if not grid.on_grid(new_pos):
                    continue
                if new_pos in seen:
                    continue
                if grid[new_pos] - grid[pos] > 1:
                    continue
                if new_pos == grid.end:
                    return step
                new_positions.append(new_pos)
                seen.add(new_pos)
        step += 1
        positions = new_positions
    return None
