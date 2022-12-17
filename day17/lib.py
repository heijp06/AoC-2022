from typing import NamedTuple
from tower import Tower
import itertools


class State(NamedTuple):
    jet: int
    rock: int


def part1(jets: str) -> int:
    tower = Tower(jets)
    for _ in range(2022):
        tower.drop_rock()
    return tower.height


def part2(jets: str) -> int:
    tower = Tower(jets)
    states: dict[State, int] = {}
    for count in range(10000):
        state = State(tower.current_jet, tower.current_rock)
        if state in states:
            print(count, state, count - states[state][0], states[state][1], tower.height)
        states[state] = count, tower.height
        tower.drop_rock()
