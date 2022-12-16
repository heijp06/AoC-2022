from typing import NamedTuple
from valve import Valve, parse

MINUTES = 30


class Probe(NamedTuple):
    pressure: int
    valve: Valve
    opened: frozenset[str]
    visited: frozenset[str]
    open_valve: bool


def part1(rows: list[str]) -> int:
    valve_aa, rates = parse(rows)
    max_pressure_left = get_max_pressure_left(rates)
    probes = [Probe(0, valve_aa, frozenset(
        {valve_aa.name}), frozenset({valve_aa.name}), False)]
    seen = set()
    max_pressure = -1
    for minute in range(1, MINUTES + 1):
        new_probes: list[Probe] = []
        for probe in probes:
            if max_pressure - probe.pressure > max_pressure_left[minute - 1]:
                continue
            if probe.open_valve:
                # open valve
                new_pressure = probe.pressure + \
                    (MINUTES - minute) * probe.valve.rate
                new_opened = frozenset({*probe.opened, probe.valve.name})
                new_visited = frozenset({probe.valve.name})
                new_probe = Probe(new_pressure, probe.valve,
                                  new_opened, new_visited, False)
                if new_probe not in seen:
                    seen.add(new_probe)
                    new_probes.append(new_probe)
                continue
            for new_valve in probe.valve.valves:
                if new_valve.name in probe.visited:
                    # been here before without opening a valve since, stop.
                    max_pressure = max(max_pressure, probe.pressure)
                    continue
                # move to next node, add it to the visited list
                new_visited = frozenset({*probe.visited, new_valve.name})
                if new_valve.rate > 0 and new_valve.name not in probe.opened:
                    # open valve next minute
                    new_probe = Probe(probe.pressure, new_valve, frozenset(
                        {*probe.opened}), new_visited, True)
                    if new_probe not in seen:
                        seen.add(new_probe)
                        new_probes.append(new_probe)
                # skip valve.
                new_probe = Probe(probe.pressure, new_valve, frozenset({
                                  *probe.opened}), new_visited, False)
                if new_probe not in seen:
                    seen.add(new_probe)
                    new_probes.append(new_probe)
        probes = new_probes
    max_pressure_of_rest = max(
        probe.pressure for probe in probes) if probes else -1
    return max(max_pressure, max_pressure_of_rest)


def part2(rows: list[str]) -> int:
    pass


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