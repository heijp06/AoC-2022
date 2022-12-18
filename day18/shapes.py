from __future__ import annotations
from typing import Any

from pyparsing import Iterable, Iterator


class Point:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def _key(self) -> tuple[int, int, int]:
        return (self.x, self.y, self.z)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Point) and self._key() == other._key()

    def __hash__(self) -> int:
        return hash(self._key())

    def __lt__(self, other: Point) -> bool:
        return self._key() < other._key()

    def __add__(self, shape: Any) -> Any:
        if isinstance(shape, Point):
            return Point(self.x + shape.x, self.y + shape.y, self.z + shape.z)
        return shape + self
    
    def __repr__(self) -> str:
        return repr(self._key())


class Side(Iterable):
    def __init__(self, point1: Point, point2: Point, point3: Point, point4: Point) -> None:
        self.points = tuple(sorted([point1, point2, point3, point4]))

    def __iter__(self) -> Iterator[Point]:
        return iter(self.points)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Side) and self.points == other.points

    def __hash__(self) -> int:
        return hash(self.points)

    def __add__(self, point: Point) -> Side:
        points = [point + p for p in self.points]
        return Side(*points)

    def __lt__(self, other: Side) -> bool:
        return self.points < other.points
    
    def __repr__(self) -> str:
        return repr(self.points)


class Cube(Iterable):
    template = (
        Side(Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 0), Point(0, 1, 0)),
        Side(Point(0, 0, 0), Point(1, 0, 0), Point(1, 0, 1), Point(0, 0, 1)),
        Side(Point(0, 0, 0), Point(0, 1, 0), Point(0, 1, 1), Point(0, 0, 1)),
        Side(Point(0, 0, 1), Point(0, 1, 1), Point(1, 1, 1), Point(1, 0, 1)),
        Side(Point(0, 1, 1), Point(0, 1, 0), Point(1, 1, 0), Point(1, 1, 1)),
        Side(Point(1, 1, 1), Point(1, 1, 0), Point(1, 0, 0), Point(1, 0, 1))
    )

    def __init__(self, offset: Point) -> None:
        self.sides = tuple(sorted([offset + side for side in Cube.template]))
        self.offset = offset

    def __iter__(self) -> Iterator[Side]:
        return iter(self.sides)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Cube) and self.sides == other.sides

    def __hash__(self) -> int:
        return hash(self.sides)
    
    def __repr__(self) -> str:
        return repr(self.offset)
