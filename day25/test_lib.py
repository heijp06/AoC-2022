import pytest
from lib import SNAFU, add, part1
from example import RESULT1, example


def test_part1() -> None:
    assert part1(example) == RESULT1


@pytest.mark.parametrize("snafu1,snafu2,expected", [
    ("2", "1", "1="),  # 2 + 1 = 3
    ("12", "2", "2-")  # 7 + 2 = 9
])
def test_add(snafu1: SNAFU, snafu2: SNAFU, expected: SNAFU) -> None:
    assert add(snafu1, snafu2) == expected
