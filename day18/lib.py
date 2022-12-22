from collections import defaultdict
import re
from grid import Grid

from shapes import Cube, Point, Side


def part1(rows: list[str]) -> int:
    sides = count_sides(rows)
    return sum(seen == 1 for seen in sides.values())


def part2(rows: list[str]) -> int:
    sides = count_sides(rows)
    grid = Grid([Cube(parse(row)) for row in rows])
    grid.find_trapped_air()
    for cube in grid.trapped_air:
        for side in cube:
            if side in sides:
                sides.pop(side)
    return sum(seen == 1 for seen in sides.values())


def count_sides(rows) -> dict[Side, int]:
    sides: dict[Side, int] = defaultdict(int)
    for row in rows:
        point = parse(row)
        cube = Cube(point)
        for side in cube:
            sides[side] += 1
    return sides


def parse(row: str) -> Point:
    fields = re.findall(r"\d+", row)
    return Point(int(fields[0]), int(fields[1]), int(fields[2]))
