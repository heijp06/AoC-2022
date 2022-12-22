from factory import parse


def part1(rows: list[str]) -> int:
    result = 0
    for row in rows:
        factory = parse(row)
        factory.build()
        level = factory.blueprint.id * factory.max_geodes
        result += level
    return result


def part2(rows: list[str]) -> int:
    result = 1
    for row in rows[:3]:
        factory = parse(row)
        factory.max_time = 32
        factory.build()
        result *= factory.max_geodes
    return result
