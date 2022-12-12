from lib import part1, part2
from example import STEPS1, STEPS2, rows


def test_part1():
    assert part1(rows) == STEPS1


def test_part2():
    assert part2(rows) == STEPS2
