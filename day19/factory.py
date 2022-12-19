from __future__ import annotations
import re
from typing import NamedTuple


def parse(row: str) -> Factory:
    fields = list(map(int, re.findall(r"\d+", row)))
    blueprint = Blueprint(
        fields[0], fields[1], fields[2], (fields[3], fields[4]), (fields[5], fields[6]))
    return Factory(blueprint)


class Blueprint(NamedTuple):
    id: int
    ore_robot: int
    clay_robot: int
    obsidian_robot: tuple[int, int]
    geode_robot: tuple[int, int]


class State(NamedTuple):
    ore: int
    clay: int
    obsidian: int
    geode: int
    ore_robots: int
    clay_robots: int
    obsidian_robots: int
    geode_robots: int


class Factory:
    def __init__(self, blueprint: Blueprint) -> None:
        self.blueprint = blueprint
        self.start_state = State(0, 0, 0, 0, 1, 0, 0, 0)
        self.max_geodes = -1

    def build(self) -> None:
        self.states = [self.start_state]
        self.seen = {self.start_state}
        for _ in range(24):
            self.new_states: list[State] = []
            for state in self.states:
                self.next_states(state)
            self.states = self.new_states

    def next_states(self, state: State) -> None:
        pass
