import pytest
from lib import part1, part2


def test_part1():
    assert part1(rows) == 13


def test_part2():
    assert part2(rows) == 1


rows = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2",
]