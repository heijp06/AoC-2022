from __future__ import annotations
import re


def parse(rows: list[str]) -> tuple[Valve, list[int]]:
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
    return valve_aa, rates


def build_system(valve: Valve, valves: dict[str, Valve], built: set[str]) -> None:
    if valve.name in built:
        return
    built.add(valve.name)
    for name in valve.valve_names:
        next_valve = valves[name]
        valve.valves.append(next_valve)
        build_system(next_valve, valves, built)


class Valve:
    def __init__(self, name: str, rate: int, valve_names: list[str]) -> None:
        self.name = name
        self.rate = rate
        self.next: list[Valve] = []
        self.valve_names = valve_names
        self.valves: list[Valve] = []

    def __repr__(self) -> str:
        return self.name
