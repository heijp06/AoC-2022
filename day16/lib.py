from solver import Solver
from valve import Valve

MINUTES = 30


def part1(rows: list[str]) -> int:
    solver = Solver(rows, 30)
    return solver.solve(get_valves(solver))


def part2(rows: list[str]) -> int:
    solver = Solver(rows, 26)
    return solver.solve()


def get_valves(solver) -> list[Valve]:
    return [valve for valve in solver.table.keys() if valve.rate > 0]
