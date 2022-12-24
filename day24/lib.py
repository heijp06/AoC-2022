from valley import parse


def part1(rows: list[str]) -> int:
    valley = parse(rows)
    valley.solve()
    return valley.min_distance


def part2(rows: list[str]) -> int:
    pass
