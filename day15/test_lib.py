import pytest
from lib import part1, part2
from example import RESULT1, RESULT2, example
from sensor import Position, Sensor, parse


def test_part1():
    assert part1(example, 10) == RESULT1


def test_part2():
    assert part2(example, 20) == RESULT2


def test_visible_columns():
    sensor = parse("Sensor at x=8, y=7: closest beacon is at x=2, y=10")

    assert sensor.position == Position(8, 7)
    assert sensor.beacon == Position(2, 10)
    assert sensor.width == 9
    assert sensor.get_visible_columns(14) == list(range(6, 11))
    assert sensor.get_visible_columns(10) == list(range(2, 15))