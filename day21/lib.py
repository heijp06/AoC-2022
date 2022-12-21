from node import parse


def part1(rows: list[str]) -> int:
    root = parse(rows)
    return root.value


def part2(rows: list[str]) -> int:
    pass
