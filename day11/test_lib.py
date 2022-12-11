from lib import part1, part2
from example import BUSINESS1, BUSINESS2, monkeys


def test_part1():
    assert part1(monkeys) == BUSINESS1


def test_part2():
    assert part2(monkeys) == BUSINESS2
