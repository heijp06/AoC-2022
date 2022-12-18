from collections import defaultdict
import re
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int
    z: int


Side = frozenset[Point]

cube = (
    frozenset((Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 0), Point(0, 1, 0))),
    frozenset((Point(0, 0, 0), Point(1, 0, 0), Point(1, 0, 1), Point(0, 0, 1))),
    frozenset((Point(0, 0, 0), Point(0, 1, 0), Point(0, 1, 1), Point(0, 0, 1))),
    frozenset((Point(0, 0, 1), Point(0, 1, 1), Point(1, 1, 1), Point(1, 0, 1))),
    frozenset((Point(0, 1, 1), Point(0, 1, 0), Point(1, 1, 0), Point(1, 1, 1))),
    frozenset((Point(1, 1, 1), Point(1, 1, 0), Point(1, 0, 0), Point(1, 0, 1)))
)


def part1(rows: list[str]) -> int:
    sides: dict[Side, int] = defaultdict(int)
    for row in rows:
        offset = parse(row)
        for side in cube:
            new_side = frozenset()
            for point in side:
                new_point = Point(point.x + offset.x, point.y +
                                  offset.y, point.z + offset.z)
                new_side = new_side | {new_point}
            sides[new_side] += 1
    return sum(seen for seen in sides.values() if seen == 1)


def part2(rows: list[str]) -> int:
    pass


def parse(row: str) -> Point:
    fields = re.findall(r"\d+", row)
    return Point(int(fields[0]), int(fields[1]), int(fields[2]))
