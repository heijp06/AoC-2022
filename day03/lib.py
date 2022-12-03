def part1(rows: list[str]) -> int:
    return sum(get_item(row) for row in rows)


def part2(rows: list[str]) -> int:
    total = 0
    for i in range(0, len(rows), 3):
        total += get_priority(get_badge(rows[i:i + 3]))
    return total


def get_item(row: str) -> int:
    length = len(row) // 2
    c1 = set(row[:length])
    c2 = set(row[length:])
    in_both = c1.intersection(c2)
    return get_priority(next(iter(in_both)))


def get_priority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord('A') + 27
    return ord(item) - ord('a') + 1


def get_badge(rows: list[str]) -> str:
    in_all = set.intersection(*map(set, rows))
    return next(iter(in_all))
