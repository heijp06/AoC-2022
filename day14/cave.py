from __future__ import annotations
from collections import namedtuple
import re

Point = namedtuple("Point", "x,y")


def parse(rows: list[str]) -> Cave:
    cave: set[Point] = set()
    y_max = 0
    for row in rows:
        coords = list(map(int, re.findall(r'\d+', row)))
        point0 = Point(coords[0], coords[1])
        for index in range(2, len(coords), 2):
            point1 = Point(coords[index], coords[index + 1])
            if point0.x == point1.x:
                if point0.y < point1.y:
                    start = point0
                    end = point1
                else:
                    start = point1
                    end = point0
                for y in range(start.y, end.y + 1):
                    cave.add(Point(point0.x, y))
                y_max = max(y_max, end.y)
            else:
                if point0.x < point1.x:
                    start = point0
                    end = point1
                else:
                    start = point1
                    end = point0
                for x in range(start.x, end.x + 1):
                    cave.add(Point(x, point0.y))
                y_max = max(y_max, point0.y)
            point0 = point1
    return Cave(cave, y_max)


class Cave:
    def __init__(self, rocks: set[Point], y_max: int) -> None:
        self._stuff = rocks
        self.y_max = y_max
        self.start = Point(500, 0)

    def add_sand(self, sand: Point) -> None:
        if sand in self._stuff:
            raise ValueError(sand)
        self._stuff.add(sand)
    
    def is_blocked(self, point: Point) -> bool:
        return point in self._stuff
