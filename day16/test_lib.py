import pytest
from lib import part1, part2
from example import RESULT1, RESULT2, SMALL1, example, small


@pytest.mark.parametrize("rows,pressure", (
    (example, RESULT1),
    (small, SMALL1)
))
def test_part1(rows: list[str], pressure: int):
    assert part1(rows) == pressure


def test_part2():
    assert part2(example) == RESULT2
