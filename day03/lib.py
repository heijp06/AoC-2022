def part1(rows: list[str]) -> int:
    return sum(get_priority(get_item(row)) for row in rows)


def part2(rows: list[str]) -> int:
    return sum(get_priority(get_badge(rows[i: i + 3])) for i in range(0, len(rows), 3))


def get_item(row: str) -> str:
    compartment_size = len(row) // 2
    compartment1 = set(row[:compartment_size])
    compartment2 = set(row[compartment_size:])
    in_both = compartment1.intersection(compartment2)
    return get_single(in_both)


def get_badge(rows: list[str]) -> str:
    in_all = set.intersection(*map(set, rows))  # type: ignore
    return get_single(in_all)


def get_single(intersection):
    return next(iter(intersection))


def get_priority(item: str) -> int:
    return ord(item) + (1 - ord('a') if item.islower() else 27 - ord('A'))
