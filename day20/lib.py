def part1(rows: list[str]) -> int:
    values = [(index, int(row)) for index, row in enumerate(rows)]
    return mix(values, 1)


def part2(rows: list[str]) -> int:
    values = [(index, 811589153 * int(row)) for index, row in enumerate(rows)]
    return mix(values, 10)


def mix(values: list[tuple[int, int]], repeat) -> int:
    new_values = list(values)
    for _ in range(repeat):
        for key, value in values:
            index = new_values.index((key, value))
            new_values.remove((key, value))
            new_index = (index + value) % (len(values) - 1)
            if new_index == 0:
                new_index = 0 if value >= 0 else (len(values) - 1)
            new_values = new_values[:new_index] + \
                [(key, value)] + new_values[new_index:]
    result = [value for _, value in new_values]
    index = result.index(0)
    return sum(result[(index + offset) % len(result)] for offset in (1000, 2000, 3000))
