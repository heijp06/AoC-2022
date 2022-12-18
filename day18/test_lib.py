import pytest
from lib import part1, part2
from example import RESULT1, RESULT2, RESULT_SMALL, example, small


@pytest.mark.parametrize("rows,area", [
    (small, RESULT_SMALL),
    (example, RESULT1)
])
def test_part1(rows: list[str], area: int):
    assert part1(rows) == area


def test_part2():
    assert part2(example) == RESULT2
