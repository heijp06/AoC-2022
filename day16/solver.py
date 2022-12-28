import heapq
from operator import attrgetter
from typing import Iterable, NamedTuple
from valve import Valve, build_distance_table


class Probe(NamedTuple):
    minutes: int
    valve: Valve


class State(NamedTuple):
    pressure: int
    opened: frozenset[Valve]
    probe: Probe

    def _key(self):
        return (self.pressure, self.opened, self.probe)

    def __eq__(self, other: object) -> bool:
        return self._key() == other._key() if isinstance(other, State) else False

    def __hash__(self) -> int:
        return hash(self._key())


class Solver:
    def __init__(self, rows: list[str], minutes: int = 26) -> None:
        self.table = build_distance_table(rows)
        self.minutes = minutes
        self.valves: list[Valve]
        self.seen: set[State]
        self.max_pressure: int
        self.states: list[tuple[int, int, State]] = []
        # See: https://en.wikipedia.org/wiki/A*_search_algorithm#Implementation_details
        self.tie_breaker = 0

    def solve(self, valves: Iterable[Valve]) -> int:
        self.valves = sorted(valves, key=attrgetter("rate"), reverse=True)
        self.seen = set()
        self.max_pressure = -1
        self.states = []
        valve_aa = next(valve for valve in self.table.keys()
                        if valve.name == "AA")
        start_state = State(0, frozenset(
            [valve_aa]), Probe(self.minutes, valve_aa))
        self.add_state(start_state)
        count = 0
        while self.states:
            neg_pressure, _, state = heapq.heappop(self.states)
            count += 1
            if count == 1000:
                count = 0
                print(f"{self.max_pressure}, {-neg_pressure}, {len(self.states)}")
            if self.max_pressure >= -neg_pressure:
                break
            self.create_new_states(state)
        return self.max_pressure

    def add_state(self, state: State):
        if state in self.seen:
            return
        self.seen.add(state)
        upper_bound = self.upper_bound(state)
        if upper_bound > self.max_pressure:
            self.tie_breaker -= 1
            heapq.heappush(
                self.states, (-upper_bound, self.tie_breaker, state))

    def create_new_states(self, state: State) -> None:
        for new_valve in self.valves:
            if new_valve in state.opened:
                continue
            cost = self.table[state.probe.valve][new_valve]
            if cost >= state.probe.minutes:
                continue
            new_probe = Probe(state.probe.minutes - cost, new_valve)
            new_pressure = state.pressure + \
                (state.probe.minutes - cost) * new_valve.rate
            new_opened = state.opened | {new_valve}
            new_state = State(new_pressure, new_opened, new_probe)
            self.add_state(new_state)
            self.max_pressure = max(self.max_pressure, new_pressure)

    def upper_bound(self, state: State) -> int:
        # calculate an upper bound for the amount of pressure that can be generated.
        # assume the cost to get to any node is 2.

        minutes = state.probe.minutes
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
