import pytest
from lib import add, part1
from example import RESULT1, example


def test_part1() -> None:
    assert part1(example) == RESULT1


@pytest.mark.parametrize("snafu1,snafu2,expected", [
    ("2", "1", "1="),  # 2 + 1 = 3
    ("12", "2", "2-")  # 7 + 2 = 9
])
def test_add(snafu1: str, snafu2: str, expected: str) -> None:
    assert add(snafu1, snafu2) == expected
