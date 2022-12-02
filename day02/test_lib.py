import pytest
from lib import part1, part2, get_rounds1, get_rounds2


def test_part1():
    assert part1(rows) == 15


def test_part2():
    assert part2(rows) == 12


def test_get_rounds1():
    assert get_rounds1(rows) == [8, 1, 6]

def test_get_rounds2():
    assert get_rounds2(rows) == [4, 1, 7]

rows = [
    "A Y",
    "B X",
    "C Z"
]
