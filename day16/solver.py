from operator import attrgetter
from typing import NamedTuple
from queue import PriorityQueue
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
        print(self.table)
        self.rates = sorted(
            valve.rate for valve in self.table.keys() if valve.rate > 0)
        self.valve_aa = next(
            valve for valve in self.table.keys() if valve.name == "AA")
        self.seen: set[State] = set()

    def solve(self) -> int:
        start_state = State(0, frozenset([self.valve_aa]), [
            Probe(MINUTES, self.valve_aa), Probe(MINUTES, self.valve_aa)])
        self.states2 = PriorityQueue()
        self.add_state(start_state)
        self.max_pressure = -1
        while self.states2.qsize():
            neg_pressure, state = self.states2.get()
            if self.states2.qsize() % 1000 == 0:
                print(f"{neg_pressure}, {self.max_pressure}, {self.states2.qsize()}")
            if self.max_pressure >= -neg_pressure:
                break
            for probe in state.probes:
                self.create_new_states(state, probe)
        return self.max_pressure

    def add_state(self, state: State):
        if state in self.seen:
            return
        self.seen.add(state)
        self.states2.put((-self.upper_bound(state), state))

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
            self.add_state(new_state)
            self.max_pressure = max(self.max_pressure, new_pressure)

    def upper_bound(self, state: State) -> None:
        # calculate an upper bound for the amount of pressure that can be generated.

        # add the time for all probes together.
        # assume the cost to get to any node is 2.

        minutes = sum(probe.minutes for probe in state.probes)
        rates = sorted(
            valve.rate for valve in self.table if valve not in state.opened)

        min_cost = 4
        pressure = state.pressure

        while rates and minutes > min_cost:
            rate = rates.pop()
            pressure += (minutes - min_cost) * rate
            minutes -= min_cost

        return pressure
