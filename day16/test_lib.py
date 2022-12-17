import pytest
from lib import get_max_pressure_left, part1, part2
from example import RESULT1, RESULT2, SMALL1, example, small
from valve import build_distance_table


@pytest.mark.parametrize("rows,pressure", (
    (example, RESULT1),
    (small, SMALL1)
))
def test_part1(rows: list[str], pressure: int):
    assert part1(rows) == pressure


def test_part2():
    assert part2(example) == RESULT2


def test_get_max_pressure_left():
    assert get_max_pressure_left([1, 3, 2]) == [
        172, 166, 160, 154, 148, 142, 136, 130, 124, 118, 112, 106, 100,
        94, 88, 82, 76, 70, 64, 58, 52, 46, 40, 34, 28, 22, 16, 11, 6, 3
    ]
