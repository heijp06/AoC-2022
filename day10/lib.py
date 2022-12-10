def part1(rows: list[str]) -> int:
    x = 1
    cycle = 1
    total = 0
    for row in rows:
        match row.split():
            case ["noop"]:
                if cycle % 40 == 20:
                    total += cycle * x
                cycle += 1
            case ["addx", value]:
                for _ in range(2):
                    if cycle % 40 == 20:
                        total += cycle * x
                    cycle += 1
                x += int(value)
    return total



def part2(rows: list[str]) -> int:
    pass
