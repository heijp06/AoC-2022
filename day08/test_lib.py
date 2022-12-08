import pytest
from lib import part1, part2, scenic_score


def test_part1():
    assert part1(rows) == 21


def test_part2():
    assert part2(rows) == 8


@pytest.mark.parametrize("coordinates,score", (
    ((1, 2), 4),
    ((3, 2), 8)
))
def test_scenic_score(coordinates: tuple[int, int], score: int) -> None:
    assert scenic_score(rows, coordinates) == score


rows = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390"
]
