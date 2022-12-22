from typing import NamedTuple
from queue import PriorityQueue
from valve import Valve, build_distance_table


class Probe(NamedTuple):
    minutes: int
    valve: Valve


class State(NamedTuple):
    pressure: int
    opened: frozenset[Valve]
    probes: list[Probe]

    def _key(self):
        return (self.pressure, self.opened, frozenset(self.probes))

    def __eq__(self, other: object) -> bool:
        return self._key() == other._key() if isinstance(other, State) else False

    def __hash__(self) -> int:
        return hash(self._key())


class Solver:
    def __init__(self, rows: list[str], part: int = 2, minutes: int = 26) -> None:
        self.table = build_distance_table(rows)
        print(self.table)
        self.valves = sorted(
            (valve for valve in self.table.keys() if valve.rate > 0),
            reverse=True)
        self.valve_aa = next(
            valve for valve in self.table.keys() if valve.name == "AA")
        self.seen: set[State] = set()
        self.max_pressure = -1
        self.states: PriorityQueue = PriorityQueue()
        self.part = part
        self.minutes = minutes

    def solve(self) -> int:
        if self.part == 2:
            start_state = State(0, frozenset([self.valve_aa]), [
                Probe(self.minutes, self.valve_aa), Probe(self.minutes, self.valve_aa)])
        else:
            start_state = State(0, frozenset([self.valve_aa]), [
                                Probe(self.minutes, self.valve_aa)])
        self.states: PriorityQueue = PriorityQueue()
        self.add_state(start_state)
        count = 0
        while not self.states.empty():
            neg_pressure, state = self.states.get()
            count += 1
            if count == 1000:
                count = 0
                print(f"{neg_pressure}, {self.max_pressure}, {self.states.qsize()}")
            if self.max_pressure >= -neg_pressure:
                break
            for index in range(len(state.probes)):
                self.create_new_states(state, index)
        return self.max_pressure

    def add_state(self, state: State):
        if state in self.seen:
            return
        self.seen.add(state)
        upper_bound = self.upper_bound(state)
        if upper_bound > self.max_pressure:
            self.states.put((-upper_bound, state))

    def create_new_states(self, state: State, index: int) -> None:
        probe = state.probes[index]
        for new_valve in self.valves:
            if new_valve in state.opened:
                continue
            cost = self.table[probe.valve][new_valve]
            if cost >= probe.minutes:
                continue
            new_probe = Probe(probe.minutes - cost, new_valve)
            if len(state.probes) == 2:
                new_probes = [new_probe, state.probes[1 - index]]
            else:
                new_probes = [new_probe]
            new_pressure = state.pressure + \
                (probe.minutes - cost) * new_valve.rate
            new_opened = state.opened | {new_valve}
            new_state = State(new_pressure, new_opened, new_probes)
            self.add_state(new_state)
            self.max_pressure = max(self.max_pressure, new_pressure)

    def upper_bound(self, state: State) -> int:
        # calculate an upper bound for the amount of pressure that can be generated.

        # add the time for all probes together.
        # assume the cost to get to any node is 2.

        minutes = sum(probe.minutes for probe in state.probes)

        min_cost = 2
        pressure = state.pressure

        valve_index = 0
        while valve_index < len(self.valves) and minutes > min_cost:
            valve = self.valves[valve_index]
            valve_index += 1
            if valve in state.opened:
                continue
            minutes -= min_cost
            pressure += minutes * valve.rate

        return pressure
