import pytest
from lib import part1, part2
from example import RESULT1, RESULT2, example, no_move


def test_part1():
    assert part1(example) == RESULT1


def test_part2():
    assert part2(example) == RESULT2

def test_no_move():
    assert part2(no_move) == 2
