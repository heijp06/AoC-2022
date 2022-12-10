from example import crt, instructions, sum_of_signal_strengths
from lib import part1, part2


def test_part1():
    assert part1(instructions) == sum_of_signal_strengths


def test_part2():
    assert part2(instructions) == crt
