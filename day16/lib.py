import datetime
from solver import Solver

MINUTES = 30


def part1(rows: list[str]) -> int:
    solver = Solver(rows, 1, 30)
    return solver.solve()


def part2(rows: list[str]) -> int:
    solver = Solver(rows, 2, 26)
    t0 = datetime.datetime.now()
    result = solver.solve()
    t1 = datetime.datetime.now()
    print(t1 - t0)
    return result
