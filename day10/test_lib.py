import pytest
from example import crt, example
from lib import part1, part2


def test_part1():
    assert part1(example) == 13140


def test_part2():
    assert part2(example) == crt
