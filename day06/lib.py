def part1(rows: list[str]) -> int:
    for i in range(len(rows) - 4):
        if len(set(rows[i:i+4])) == 4:
            return i + 4
    return -1


def part2(rows: list[str]) -> int:
    for i in range(len(rows) - 14):
        if len(set(rows[i:i+14])) == 14:
            return i + 14
    return -1
