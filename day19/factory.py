from __future__ import annotations
import heapq
import re
from typing import NamedTuple, Optional


def parse(row: str) -> Factory:
    fields = list(map(int, re.findall(r"\d+", row)))
    blueprint = Blueprint(
        fields[0], fields[1], fields[2], (fields[3], fields[4]), (fields[5], fields[6]))
    return Factory(blueprint)


class Blueprint(NamedTuple):
    id: int
    ore_robot_cost: int
    clay_robot_cost: int
    obsidian_robot_cost: tuple[int, int]
    geode_robot_cost: tuple[int, int]


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

    def update(self,  # pylint: disable=too-many-arguments
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
            time or self.time,
            ore or self.ore,
            clay or self.clay,
            obsidian or self.obsidian,
            geodes or self.geodes,
            ore_robots or self.ore_robots,
            clay_robots or self.clay_robots,
            obsidian_robots or self.obsidian_robots,
            geode_robots or self.geode_robots,
        )


class Factory:
    def __init__(self, blueprint: Blueprint) -> None:
        self.blueprint = blueprint
        self.start_state = State(1, 0, 0, 0, 0, 1, 0, 0, 0)
        self.max_geodes = -1
        self.seen: set[State] = set()
        self.max_time = 24
        self.states: list[tuple[int, int, State]]

    def build(self) -> None:
        self.states = []
        self.add_state(self.start_state)
        while self.states:
            neg_upper_bound, _, state = heapq.heappop(self.states)
            if self.max_geodes >= -neg_upper_bound:
                break
            self.next_states(state)

    def add_state(self, state: State):
        if state in self.seen:
            return
        self.seen.add(state)
        heapq.heappush(self.states, (-self.upper_bound(state), -state.time, state))

    def next_states(self, state: State) -> None:
        # increase time
        new_state = state.update(state.time + 1)
        new_states = [self.collect(new_state)]

        # if you want to build any robot first spend ore + rest.
        new_states += self.build_ore_robot(new_state)
        new_states += self.build_clay_robot(new_state)
        new_states += self.build_obsidian_robot(new_state)
        new_states += self.build_geode_robot(new_state)

        # only enque if there still is time left.
        for new_state in new_states:
            if new_state.time <= self.max_time:
                self.add_state(new_state)

    def build_ore_robot(self, state: State) -> list[State]:
        if state.ore < self.blueprint.ore_robot_cost:
            return []
        new_state = self.collect(state)
        return [new_state.update(
            ore=new_state.ore - self.blueprint.ore_robot_cost,
            ore_robots=new_state.ore_robots + 1
        )]

    def build_clay_robot(self, state: State) -> list[State]:
        if state.ore < self.blueprint.clay_robot_cost:
            return []
        new_state = self.collect(state)
        return [new_state.update(
            ore=new_state.ore - self.blueprint.clay_robot_cost,
            clay_robots=new_state.clay_robots + 1
        )]

    def build_obsidian_robot(self, state: State) -> list[State]:
        if state.ore < self.blueprint.obsidian_robot_cost[0]:
            return []
        if state.clay < self.blueprint.obsidian_robot_cost[1]:
            return []
        new_state = self.collect(state)
        return [new_state.update(
            ore=new_state.ore - self.blueprint.obsidian_robot_cost[0],
            clay=new_state.clay - self.blueprint.obsidian_robot_cost[1],
            obsidian_robots=new_state.obsidian_robots + 1
        )]

    def build_geode_robot(self, state: State) -> list[State]:
        if state.ore < self.blueprint.geode_robot_cost[0]:
            return []
        if state.obsidian < self.blueprint.geode_robot_cost[1]:
            return []
        new_state = self.collect(state)
        return [new_state.update(
            ore=new_state.ore - self.blueprint.geode_robot_cost[0],
            obsidian=new_state.obsidian - self.blueprint.geode_robot_cost[1],
            geode_robots=new_state.geode_robots + 1
        )]

    def collect(self, state: State) -> State:
        new_state = state.update(
            ore=state.ore + state.ore_robots,
            clay=state.clay + state.clay_robots,
            obsidian=state.obsidian + state.obsidian_robots,
            geodes=state.geodes + state.geode_robots
        )
        self.max_geodes = max(self.max_geodes, new_state.geodes)
        return new_state

    def upper_bound(self, state: State) -> int:
        # calculate an upper bound for the amount of geodes that can be collected.

        # assume each robot type has there own stash of ore to use.
        # also assume the factory can build more than 1 robot at a time.
        # this will overestimate what can be build, but makes calculation simpler.
        ore_robot_ore = state.ore
        clay_robot_ore = state.ore
        obsidian_robot_ore = state.ore
        geode_robot_ore = state.ore

        while state.time <= self.max_time:
            # update time.
            state = state.update(time=state.time + 1)

            # decide to build robots and incur the cost.
            build_ore_robot = False
            build_clay_robot = False
            build_obsidian_robot = False
            build_geode_robot = False
            if ore_robot_ore >= self.blueprint.ore_robot_cost:
                ore_robot_ore -= self.blueprint.ore_robot_cost
                build_ore_robot = True
            if clay_robot_ore >= self.blueprint.clay_robot_cost:
                clay_robot_ore -= self.blueprint.clay_robot_cost
                build_clay_robot = True
            if (obsidian_robot_ore >= self.blueprint.obsidian_robot_cost[0]
                    and state.clay >= self.blueprint.obsidian_robot_cost[1]):
                obsidian_robot_ore -= self.blueprint.obsidian_robot_cost[0]
                state = state.update(
                    clay=state.clay - self.blueprint.obsidian_robot_cost[1])
                build_obsidian_robot = True
            if (geode_robot_ore >= self.blueprint.geode_robot_cost[0]
                    and state.obsidian >= self.blueprint.geode_robot_cost[1]):
                geode_robot_ore -= self.blueprint.geode_robot_cost[0]
                state = state.update(
                    obsidian=state.obsidian - self.blueprint.geode_robot_cost[1])
                build_geode_robot = True

            # harvest the minerals and build the robots.
            ore_robot_ore += state.ore_robots
            clay_robot_ore += state.ore_robots
            obsidian_robot_ore += state.ore_robots
            geode_robot_ore += state.ore_robots
            state = state.update(
                clay=state.clay + state.clay_robots,
                obsidian=state.obsidian + state.obsidian_robots,
                geodes=state.geodes + state.geode_robots,
                ore_robots=state.ore_robots + build_ore_robot,
                clay_robots=state.clay_robots + build_clay_robot,
                obsidian_robots=state.obsidian_robots + build_obsidian_robot,
                geode_robots=state.geode_robots + build_geode_robot)

        return state.geodes
