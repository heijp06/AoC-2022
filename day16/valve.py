from __future__ import annotations
from itertools import product
import re


class Valve:
    def __init__(self, name: str, rate: int, valve_names: list[str]) -> None:
        self.name = name
        self.rate = rate
        self.next: list[Valve] = []
        self.valve_names = valve_names
        self.valves: list[Valve] = []

    def __repr__(self) -> str:
        return self.name


Table = dict[Valve, dict[Valve, int]]


def parse(rows: list[str]) -> list[Valve]:
    valves: dict[str, Valve] = {}
    rates = []
    for row in rows:
        result = re.match(
            r"Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)", row)
        assert result is not None
        name = result[1]
        rate = int(result[2])
        rates.append(rate)
        valve_names = re.split(r", ", result[3])
        valves[name] = Valve(name, rate, valve_names)
    valve_aa = valves["AA"]
    build_system(valve_aa, valves, set())
    return list(valves.values())


def build_distance_table(rows: list[str]) -> Table:
    valves = parse(rows)
    nodes = [valve for valve in valves if valve.name == "AA" or valve.rate > 0]
    distance_table: Table = {valve: {} for valve in nodes}
    for start, end in product(nodes, repeat=2):
        distance_table[start][end] = get_distance(start, end)
    return distance_table


def get_distance(start: Valve, end: Valve) -> int:
    if start == end:
        return 0
    distance = 0
    valves = {start}
    seen = {start}
    while valves:
        distance += 1
        new_valves = set()
        for valve in valves:
            for new_valve in valve.valves:
                if new_valve == end:
                    return distance + (new_valve.rate > 0)
                if new_valve in seen:
                    continue
                seen.add(new_valve)
                new_valves.add(new_valve)
        valves = new_valves
    raise ValueError("Cannot find end.")


def build_system(valve: Valve, valves: dict[str, Valve], built: set[str]) -> None:
    if valve.name in built:
        return
    built.add(valve.name)
    for name in valve.valve_names:
        next_valve = valves[name]
        valve.valves.append(next_valve)
        build_system(next_valve, valves, built)
