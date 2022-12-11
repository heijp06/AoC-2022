from math import lcm
from monkey import parse


def part1(rows: list[str]) -> int:
    return monkey_business(rows, 20, 3)


def part2(rows: list[str]) -> int:
    return monkey_business(rows, 10000, 1)


def monkey_business(rows: list[str], rounds: int, divisor: int) -> int:
    monkeys = parse(rows, divisor)
    modulus = lcm(*(monkey.modulus for monkey in monkeys))
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                index, item = monkey.inspect()
                item %= modulus
                monkeys[index].items.append(item)
    levels = sorted(monkey.business for monkey in monkeys)
    return levels[-1] * levels[-2]
