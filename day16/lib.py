from typing import NamedTuple
from valve import Valve, parse


class Probe(NamedTuple):
    pressure: int
    valve: Valve
    opened: set[str]
    visited: set[str]
    open_valve: bool


def part1(rows: list[str]) -> int:
    MINUTES = 30
    valve_aa = parse(rows)
    probes = [Probe(0, valve_aa, {valve_aa.name}, {valve_aa.name}, False)]
    max_pressure = -1
    for minute in range(1, MINUTES + 1):
        new_probes: list[Probe] = []
        for probe in probes:
            if probe.open_valve:
                # open valve
                new_pressure = probe.pressure + (MINUTES - minute) * probe.valve.rate
                new_opened = {*probe.opened, probe.valve.name}
                new_visited = {probe.valve.name}
                new_probes.append(Probe(new_pressure, probe.valve, new_opened, new_visited, False))
                continue
            for new_valve in probe.valve.valves:
                if new_valve.name in probe.visited:
                    # been here before without opening a valve since, stop.
                    max_pressure = max(max_pressure, probe.pressure)
                    continue
                # move to next node, add it to the visited list
                new_visited = {*probe.visited, new_valve.name}
                if new_valve.rate > 0 and new_valve.name not in probe.opened:
                    # open valve next minute
                    new_probes.append(Probe(probe.pressure, new_valve, {*probe.opened}, new_visited, True))
                # skip valve.
                new_probes.append(Probe(probe.pressure, new_valve, {*probe.opened}, {*new_visited}, False))
        probes = new_probes
    max_pressure_of_rest = max(probe.pressure for probe in probes) if probes else -1
    return max(max_pressure, max_pressure_of_rest)


def part2(rows: list[str]) -> int:
    pass


                # note that calculations may change because minute is now 1 based.
                # maybe add bool to Probe to indicate opening on next turn
                # also a valve does not need to be opened (CC in example)

                # probes and new_probes probably should be sets
                # maybe also add a set for all probes ever seen

                # register the score of a probe before it dies
                # (it may not be able to move anywhere but still have the max score.)

                # if not opened, open
                # else move on

                # if open, add score

                # old code for reference
                # new_score = probe.score + new_valve.rate * (MINUTES - minute)
                # if new_valve.rate > 0:
                #     new_opened = {*probe.opened, new_valve.name}
                #     new_visited = {new_valve.name}
                # else:
                #     new_opened = set(probe.opened)
                #     new_visited = {*probe.visited, new_valve.name}
                # new_probes.append((Probe(new_score, new_valve, new_opened, new_visited)))