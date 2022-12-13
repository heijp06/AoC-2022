import pytest
from lib import part1, part2
from example import RESULT1, RESULT2, example


def test_part1():
    assert part1(example) == RESULT1


def test_part2():
    assert part2(example) == RESULT2
