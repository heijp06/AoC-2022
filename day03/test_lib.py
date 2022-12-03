import pytest
from lib import part1, part2, get_badge, get_item


data = [
    ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
    ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
    ("PmmdzqPrVvPwwTWBwg", "P"),
    ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
    ("ttgJtRGJQctTZtZT", "t"),
    ("CrZsJsPPZsGzwwsLwLmpwMDw", "s")
]


def test_part1():
    assert part1(get_rucksacks(data)) == 157


def test_part2():
    assert part2(get_rucksacks(data)) == 70


@pytest.mark.parametrize("rucksack,item", data)
def test_get_item(rucksack: str, item: str) -> None:
    assert get_item(rucksack) == item


@pytest.mark.parametrize("tuples,badge", (
    (data[:3], "r"),
    (data[3:], "Z"),
))
def test_get_badge(tuples: list[tuple[str, str]], badge: str):
    assert get_badge(get_rucksacks(tuples)) == badge


def get_rucksacks(tuples: list[tuple[str, str]]):
    return [tuple[0] for tuple in tuples]
