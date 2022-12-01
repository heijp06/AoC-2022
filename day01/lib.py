def part1(rows: list[str]) -> int:
    calories = get_calories(rows)
    return calories[0]


def part2(rows: list[str]) -> int:
    calories = get_calories(rows)
    return sum(calories[:3])


def get_calories(rows: list[str]) -> list[int]:
    calories = []
    total = 0

    for row in rows:
        if row:
            total += int(row)
            continue
        calories.append(total)
        total = 0

    if total:
        calories.append(total)

    return sorted(calories, reverse=True)
