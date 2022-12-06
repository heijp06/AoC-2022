import pytest
from lib import part1, part2


data = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", (7, 19)),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", (5, 23)),
    ("nppdvjthqldpwncqszvftbrmjlhg", (6, 23)),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", (10, 29)),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", (11, 26))
]


@pytest.mark.parametrize("datastream,positions", data)
def test_part1(datastream: str, positions: tuple[int, int]) -> None:
    assert part1(datastream) == positions[0]


@pytest.mark.parametrize("datastream,positions", data)
def test_part2(datastream: str, positions: tuple[int, int]) -> None:
    assert part2(datastream) == positions[1]
