def part1(data: str) -> int:
    return find_unique_sequence(data, 4)


def part2(data: str) -> int:
    return find_unique_sequence(data, 14)


def find_unique_sequence(data: str, length: int) -> int:   # sourcery skip: use-next
    for i in range(len(data) - length):
        if len(set(data[i:i+length])) == length:
            return i + length
    raise ValueError(f"Unique sequence of length {length} not found.")
