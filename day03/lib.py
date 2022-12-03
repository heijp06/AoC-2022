def part1(rows: list[str]) -> int:
    return sum(get_priority(get_item(row)) for row in rows)


def part2(rows: list[str]) -> int:
    return sum(get_priority(get_badge(rows[i: i + 3])) for i in range(0, len(rows), 3))


def get_item(row: str) -> str:
    compartment_size = len(row) // 2
    return get_shared_element([row[:compartment_size], row[compartment_size:]])


def get_badge(rows: list[str]) -> str:
    return get_shared_element(rows)


def get_shared_element(rows: list[str]) -> str:
    return get_single(set.intersection(*map(set, rows)))  # type: ignore


def get_single(intersection: set[str]) -> str:
    return next(iter(intersection))


def get_priority(item: str) -> int:
    return ord(item) + (1 - ord('a') if item.islower() else 27 - ord('A'))
