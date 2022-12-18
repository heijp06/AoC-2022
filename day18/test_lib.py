import pytest
from grid import Grid
from lib import parse, part1, part2
from example import RESULT1, RESULT2, RESULT_SMALL, example, small
from shapes import Cube, Point


@pytest.mark.parametrize("rows,area", [
    (small, RESULT_SMALL),
    (example, RESULT1)
])
def test_part1(rows: list[str], area: int):
    assert part1(rows) == area


def test_part2():
    assert part2(example) == RESULT2


def test_outside_air():
    cube = Cube(Point(1, 1, 1))
    grid = Grid([cube])
    grid.create_border()
    assert grid.outside_air == {
        Cube(Point(x, y, z))
        for x in range(3)
        for y in range(3)
        for z in range(3)
        if (x, y, z) != (1, 1, 1)
    }


def test_trapped_air():
    cubes = [Cube(parse(row)) for row in example]
    grid = Grid(cubes)
    grid.find_trapped_air()
    assert grid.trapped_air == {Cube(Point(2, 2, 5))}


def test_trapped_air2():
    cubes = [
        Cube(Point(x, y, z))
        for x in range(3)
        for y in range(3)
        for z in range(3)
        if (x, y, z) != (1, 1, 1)
    ]
    cubes.append(Cube(Point(3, 0, 0)))
    grid = Grid(cubes)
    grid.find_trapped_air()
    assert grid.trapped_air == {Cube(Point(1, 1, 1))}
