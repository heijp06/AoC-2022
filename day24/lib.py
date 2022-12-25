from valley import Valley


def part1(rows: list[str]) -> int:
    valley = Valley(rows)
    valley.solve(1)
    if valley.min_distance is None:
        raise ValueError("No min distance found.")
    return valley.min_distance


def part2(rows: list[str]) -> int:
    valley = Valley(rows)
    valley.solve(2)
    if valley.min_distance is None:
        raise ValueError("No min distance found.")
    return valley.min_distance
