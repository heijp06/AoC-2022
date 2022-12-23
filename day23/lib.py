import datetime
from itertools import count
from grid import parse


def part1(rows: list[str]) -> int:
    grid = parse(rows)
    for _ in range(10):
        grid.do_round()

    return grid.get_height() * grid.get_width() - len(grid.elves)


def part2(rows: list[str]) -> int:
    grid = parse(rows)
    t0 = datetime.datetime.now()
    for number in count(1):
        if grid.do_round():
            t1 = datetime.datetime.now()
            print(t1 - t0)
            return number
    raise ValueError("Escaped infinite loop.")
