from monkey import parse
from math import prod


def part1(rows: list[str]) -> int:
    monkeys = parse(rows, 3)
    for _ in range(20):
        for monkey in monkeys:
            while(monkey.items):
                index, item = monkey.inspect()
                monkeys[index].items.append(item)
    levels = sorted(monkey.business for monkey in monkeys)
    return levels[-1] * levels[-2]


def part2(rows: list[str]) -> int:
    monkeys = parse(rows, 1)
    modulus = prod(monkey.modulus for monkey in monkeys)
    for _ in range(10000):
        for monkey in monkeys:
            while(monkey.items):
                index, item = monkey.inspect()
                item %= modulus
                monkeys[index].items.append(item)
    levels = sorted(monkey.business for monkey in monkeys)
    return levels[-1] * levels[-2]
