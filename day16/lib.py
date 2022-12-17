from typing import NamedTuple
from solver import Solver

from valve import Valve, parse

MINUTES = 30


def part1(rows: list[str]) -> int:
    pass


def part2(rows: list[str]) -> int:
    solver = Solver(rows)
    return solver.solve()


def get_max_pressure_left(rates: list[int]):
    down = sorted(rates)
    pressure_left: list[int] = [0]
    pressure = 0
    for _ in range(0, MINUTES, 2):
        if down:
            pressure += down.pop()
        pressure_left.insert(0, pressure_left[0] + pressure)
        pressure_left.insert(0, pressure_left[0] + pressure)
    pressure_left.pop()
    return pressure_left