import re


def part1(rows: list[str]) -> int:
    total = 0
    for row in rows:
        (s1, e1), (s2, e2) = parse_section_pair(row)
        total += contains((s1, e1), (s2, e2))
    return total


def part2(rows: list[str]) -> int:
    total = 0
    for row in rows:
        (s1, e1), (s2, e2) = parse_section_pair(row)
        total += overlaps((s1, e1), (s2, e2))
    return total


def parse_section_pair(row: str) -> tuple[tuple[int, int], tuple[int, int]]:
    s1, e1, s2, e2 = re.split("[,-]", row)
    return (int(s1), int(e1)), (int(s2), int(e2))


def contains(section1: tuple[int, int], section2: tuple[int, int]) -> bool:
    s1, e1 = section1
    s2, e2 = section2
    return s1 <= s2 and e1 >= e2 or s2 <= s1 and e2 >= e1

def overlaps(section1: tuple[int, int], section2: tuple[int, int]) -> bool:
    s1, e1 = section1
    s2, e2 = section2
    set1 = set(range(s1, e1 + 1))
    set2 = set(range(s2, e2 + 1))
    return len(set1.intersection(set2)) > 0
