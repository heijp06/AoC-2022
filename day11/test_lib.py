import pytest
from lib import part1, part2
from example import business1, business2, monkeys


def test_part1():
    assert part1(monkeys) == business1


def test_part2():
    assert part2(monkeys) == business2
