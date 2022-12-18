from collections import defaultdict
import re

from shapes import Cube, Point, Side


def part1(rows: list[str]) -> int:
    sides: dict[Side, int] = defaultdict(int)
    for row in rows:
        point = parse(row)
        cube = Cube(point)
        for side in cube:
            sides[side] += 1
    return sum(seen for seen in sides.values() if seen == 1)


def part2(rows: list[str]) -> int:
    pass


def parse(row: str) -> Point:
    fields = re.findall(r"\d+", row)
    return Point(int(fields[0]), int(fields[1]), int(fields[2]))
