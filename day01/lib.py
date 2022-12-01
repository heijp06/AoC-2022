def part1(rows: list[str]) -> int:
    maximum = 0
    total = 0
    for row in rows:
        if row:
            total += int(row)
            continue
        if total > maximum:
            maximum = total
        total = 0
    if total > maximum:
        maximum = total
    return maximum


def part2(rows: list[str]) -> int:
    elves = []
    total = 0
    for row in rows:
        if row:
            total += int(row)
            continue
        elves.append(total)
        total = 0
    elves.append(total)
    elves.sort(reverse=True)
    return sum(elves[:3])

