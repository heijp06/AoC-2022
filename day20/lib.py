def part1(rows: list[str]) -> int:
    return mix(rows, 1, 1)


def part2(rows: list[str]) -> int:
    return mix(rows, 811589153, 10)


def mix(rows: list[str], key: int, repeat: int) -> int:
    pairs = [(ref, key * int(row)) for ref, row in enumerate(rows)]
    length = len(pairs)
    new_pairs = list(pairs)
    for _ in range(repeat):
        for ref, value in pairs:
            index = new_pairs.index((ref, value))
            new_pairs.remove((ref, value))
            new_index = (index + value) % (length - 1)
            if new_index == 0 and value < 0:
                new_index = length - 1
            new_pairs.insert(new_index, (ref, value))
    result = [value for _, value in new_pairs]
    index = result.index(0)
    return sum(result[(index + offset) % length] for offset in (1000, 2000, 3000))
