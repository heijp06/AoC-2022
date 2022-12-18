from __future__ import annotations
from collections import defaultdict
from collections.abc import Iterable
import re
from typing import Iterator, NamedTuple


class Point(NamedTuple):
    x: int
    y: int
    z: int


class Side(Iterable):
    def __init__(self, point1: Point, point2: Point, point3: Point, point4: Point) -> None:
        self.points = tuple(sorted([point1, point2, point3, point4]))

    def __iter__(self) -> Iterator[Point]:
        return iter(self.points)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Side) and self.points == other.points

    def __hash__(self) -> int:
        return hash(self.points)


cube = (
    Side(Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 0), Point(0, 1, 0)),
    Side(Point(0, 0, 0), Point(1, 0, 0), Point(1, 0, 1), Point(0, 0, 1)),
    Side(Point(0, 0, 0), Point(0, 1, 0), Point(0, 1, 1), Point(0, 0, 1)),
    Side(Point(0, 0, 1), Point(0, 1, 1), Point(1, 1, 1), Point(1, 0, 1)),
    Side(Point(0, 1, 1), Point(0, 1, 0), Point(1, 1, 0), Point(1, 1, 1)),
    Side(Point(1, 1, 1), Point(1, 1, 0), Point(1, 0, 0), Point(1, 0, 1))
)


def part1(rows: list[str]) -> int:
    sides: dict[Side, int] = defaultdict(int)
    for row in rows:
        offset = parse(row)
        for side in cube:
            points: list[Point] = []
            for point in side:
                new_point = Point(point.x + offset.x, point.y +
                                  offset.y, point.z + offset.z)
                points.append(new_point)
            sides[Side(*points)] += 1
    return sum(seen for seen in sides.values() if seen == 1)


def part2(rows: list[str]) -> int:
    pass


def parse(row: str) -> Point:
    fields = re.findall(r"\d+", row)
    return Point(int(fields[0]), int(fields[1]), int(fields[2]))
