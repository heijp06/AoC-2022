from example import crt, instructions, SUM_OF_SIGNAL_STRENGTHS
from lib import part1, part2


def test_part1():
    assert part1(instructions) == SUM_OF_SIGNAL_STRENGTHS


def test_part2():
    assert part2(instructions) == crt
