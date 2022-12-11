from monkey import Monkey, parse


def part1(rows: list[str]) -> int:
    monkeys = parse(rows)
    for _ in range(20):
        for monkey in monkeys:
            while(monkey.items):
                index, item = monkey.inspect()
                monkeys[index].items.append(item)
    levels = sorted(monkey.business for monkey in monkeys)
    return levels[-1] * levels[-2]


def part2(rows: list[str]) -> int:
    pass
