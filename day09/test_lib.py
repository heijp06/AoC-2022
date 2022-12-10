import pytest
from lib import part1, part2
from examples import large, small


def test_part1():
    assert part1(small) == 13


@pytest.mark.parametrize("rows,visited", (
    (small, 1),
    (large, 36)
))
def test_part2(rows: list[str], visited: int):
    assert part2(rows) == visited
