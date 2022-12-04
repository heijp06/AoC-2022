from typing import Callable
import re

Section = set[int]


def part1(rows: list[str]) -> int:
    return count(rows, contains)


def part2(rows: list[str]) -> int:
    return count(rows, overlaps)


def count(rows: list[str], func: Callable[[Section, Section], bool]) -> int:
    return sum(func(*parse_section_pair(row)) for row in rows)


def parse_section_pair(row: str) -> tuple[Section, Section]:
    start1, end1, start2, end2 = re.split("[,-]", row)
    section1 = set(range(int(start1), int(end1) + 1))
    section2 = set(range(int(start2), int(end2) + 1))
    return section1, section2


def contains(section1: Section, section2: Section) -> bool:
    return section1.issubset(section2) or section2.issubset(section1)


def overlaps(section1: Section, section2: Section) -> bool:
    return len(section1.intersection(section2)) > 0
