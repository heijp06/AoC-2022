import itertools
from solver import Solver
from valve import Valve

MINUTES = 30


def part1(rows: list[str]) -> int:
    solver = Solver(rows, 30)
    return solver.solve(get_valves(solver))


def part2(rows: list[str]) -> int:
    solver = Solver(rows, 26)
    valves = get_valves(solver)
    max_pressure = -1
    for count in range(len(valves) // 2 + 1):
        for valves_probe1 in itertools.combinations(valves, count):
            valves_probe2 = [
                valve for valve in valves if valve not in valves_probe1]
            pressure1 = solver.solve(valves_probe1)
            pressure2 = solver.solve(valves_probe2)
            max_pressure = max(max_pressure, pressure1 + pressure2)
    return max_pressure


def get_valves(solver) -> list[Valve]:
    return [valve for valve in solver.table.keys() if valve.rate > 0]
