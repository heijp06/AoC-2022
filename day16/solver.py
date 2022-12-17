from typing import NamedTuple
from valve import Valve, build_distance_table

MINUTES = 26


class Probe(NamedTuple):
    minutes: int
    valve: Valve


class State(NamedTuple):
    pressure: int
    opened: frozenset[Valve]
    probes: list[Probe]

    def __key(self):
        return (self.pressure, self.opened, frozenset(self.probes))

    def __eq__(self, other: object) -> bool:
        return self.__key == other.__key if isinstance(other, State) else False

    def __hash__(self) -> int:
        return hash(self.__key)


class Solver:
    def __init__(self, rows: list[str]) -> None:
        self.table = build_distance_table(rows)
        self.rates = sorted(
            valve.rate for valve in self.table.keys() if valve.rate > 0)
        self.valve_aa = next(
            valve for valve in self.table.keys() if valve.name == "AA")

    def solve(self) -> int:
        start_state = State(0, frozenset([self.valve_aa]), [
            Probe(MINUTES, self.valve_aa), Probe(MINUTES, self.valve_aa)])
        states = {start_state}
        self.seen = {start_state}
        self.max_pressure = -1
        while states:
            print(len(states))
            self.new_states = set()
            for state in states:
                for probe in state.probes:
                    self.create_new_states(state, probe)
            states = self.new_states
        return self.max_pressure

    def create_new_states(self, state: State, probe: Probe) -> None:
        for new_valve in self.table.keys():
            if new_valve in state.opened:
                continue
            cost = self.table[probe.valve][new_valve]
            if cost >= probe.minutes:
                continue
            new_probe = Probe(probe.minutes - cost, new_valve)
            new_probes = list(state.probes)
            new_probes.remove(probe)
            new_probes.append(new_probe)
            new_pressure = state.pressure + \
                (probe.minutes - cost) * new_valve.rate
            new_opened = state.opened | {new_valve}
            new_state = State(new_pressure, new_opened, new_probes)
            if new_state in self.seen:
                continue
            self.seen.add(new_state)
            self.new_states.add(new_state)
            self.max_pressure = max(self.max_pressure, new_pressure)
