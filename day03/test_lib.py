import pytest
from lib import part1, part2, get_badge


def test_part1():
    assert part1(rows) == 157


def test_part2():
    assert part2(rows) == 70


def test_get_badge():
    assert get_badge(rows[:3]) == "r"
    assert get_badge(rows[3:]) == "Z"


rows = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]
