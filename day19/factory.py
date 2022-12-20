from __future__ import annotations
import re
from typing import NamedTuple, Optional


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
    time: int
    ore: int
    clay: int
    obsidian: int
    geodes: int
    ore_robots: int
    clay_robots: int
    obsidian_robots: int
    geode_robots: int

    def update_state(self,
                     time: Optional[int] = None,
                     ore: Optional[int] = None,
                     clay: Optional[int] = None,
                     obsidian: Optional[int] = None,
                     geodes: Optional[int] = None,
                     ore_robots: Optional[int] = None,
                     clay_robots: Optional[int] = None,
                     obsidian_robots: Optional[int] = None,
                     geode_robots: Optional[int] = None
                     ) -> State:
        return State(
            self.time or time,
            self.ore or ore,
            self.clay or clay,
            self.obsidian or obsidian,
            self.geodes or geodes,
            self.ore_robots or ore_robots,
            self.clay_robots or clay_robots,
            self.obsidian_robots or obsidian_robots,
            self.geode_robots or geode_robots,
        )


class Factory:
    def __init__(self, blueprint: Blueprint) -> None:
        self.blueprint = blueprint
        self.start_state = State(1, 0, 0, 0, 0, 1, 0, 0, 0)
        self.max_geodes = -1

    def build(self) -> None:
        self.states = [self.start_state]
        self.seen = {self.start_state}
        self.new_states: list[State] = []
        for state in self.states:
            self.next_states(state)
        self.states = self.new_states

    def next_states(self, state: State) -> None:
        # increase time
        new_state = state.update_state(state.time + 1)

        # if you want to build any robot first spend ore + rest.

        # collect what the existing robots are producing

        # if time > 24 stop
