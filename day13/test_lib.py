import pytest
from lib import part1, part2
from example import rows, RESULT1, RESULT2


def test_part1():
    assert part1(rows) == RESULT1


def test_part2():
    assert part2(rows) == RESULT2
