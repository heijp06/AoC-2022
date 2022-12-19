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
    pass
