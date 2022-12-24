from __future__ import annotations
import itertools
from math import lcm
from queue import PriorityQueue
from typing import NamedTuple, Optional


def parse(rows: list[str]) -> Valley:
    height = len(rows)
    width = len(rows[0])
    up: set[Position] = set()
    down: set[Position] = set()
    right: set[Position] = set()
    left: set[Position] = set()
    walls: set[Position] = {Position(-1, 1), Position(height, width - 2)}
    for row, column in itertools.product(range(height), range(width)):
        position = Position(row, column)
        match rows[row][column]:
            case "#":
                walls.add(position)
            case ">":
                right.add(position)
            case "v":
                down.add(position)
            case "<":
                left.add(position)
            case "^":
                up.add(position)
    open_spots: list[set[Position]] = []
    for _ in range(lcm(height - 2, width - 2)):
        open_spots.append({
            Position(row, column)
            for row in range(height)
            for column in range(width)
            if (
                Position(row, column) not in walls and
                Position(row, column) not in right and
                Position(row, column) not in down and
                Position(row, column) not in left and
                Position(row, column) not in up
            )
        })
        right = move_right(right, width)
        down = move_down(down, height)
        left = move_left(left, width)
        up = move_up(up, height)
    start = Position(0, 1)
    end = Position(height - 1, width - 2)
    return Valley(open_spots, start, end)


def move_right(positions: set[Position], width: int) -> set[Position]:
    new_positions: set[Position] = set()
    for position in positions:
        new_position = position + Position(0, 1)
        if new_position.column > width - 2:
            new_position = Position(position.row, 1)
        new_positions.add(new_position)
    return new_positions


def move_down(positions: set[Position], height: int) -> set[Position]:
    new_positions: set[Position] = set()
    for position in positions:
        new_position = position + Position(1, 0)
        if new_position.row > height - 2:
            new_position = Position(1, position.column)
        new_positions.add(new_position)
    return new_positions


def move_left(positions: set[Position], width: int) -> set[Position]:
    new_positions: set[Position] = set()
    for position in positions:
        new_position = position + Position(0, -1)
        if new_position.column < 1:
            new_position = Position(position.row, width - 2)
        new_positions.add(new_position)
    return new_positions


def move_up(positions: set[Position], height: int) -> set[Position]:
    new_positions: set[Position] = set()
    for position in positions:
        new_position = position + Position(-1, 0)
        if new_position.row < 1:
            new_position = Position(height - 2, position.column)
        new_positions.add(new_position)
    return new_positions


class Position:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column

    def _key(self) -> tuple[int, int]:
        return (self.row, self.column)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Position) and self._key() == other._key()

    def __hash__(self) -> int:
        return hash(self._key())

    def __add__(self, other: Position) -> Position:
        return Position(self.row + other.row, self.column + other.column)

    def __repr__(self) -> str:
        return repr(self._key())

    def __lt__(self, other: Position) -> bool:
        return self._key() < other._key()

class State(NamedTuple):
    steps: int
    position: Position


class Valley:
    def __init__(self, open_spots: list[set[Position]], start: Position, end: Position) -> None:
        self.open_spots = open_spots
        self.start = start
        self.end = end
        self.states: PriorityQueue = PriorityQueue()
        self.seen: set[State] = set()
        self.min_distance: Optional[int] = None

    def solve(self) -> None:
        self.seen.clear()
        start_state = State(0, self.start)
        self.add_state(start_state)
        self.min_distance = None
        while not self.states.empty():
            min_distance, state = self.states.get()
            if self.min_distance and self.min_distance <= min_distance:
                break
            self.create_new_states(state)

    def add_state(self, state: State):
        if state in self.seen:
            return
        if state.position == self.end:
            self.min_distance = min(self.min_distance or state.steps, state.steps)
            return
        self.seen.add(state)
        self.states.put((self.get_min_distance(state), state))

    def get_min_distance(self, state: State) -> int:
        return (
            abs(self.end.row - state.position.row)
            + abs(self.end.column - state.position.column)
            + state.steps
        )

    def create_new_states(self, state: State) -> None:
        for direction in itertools.starmap(Position, [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]):
            new_steps = state.steps + 1
            new_position = state.position + direction
            if self.is_open_spot(new_steps, new_position):
                self.add_state(State(new_steps, new_position))

    def is_open_spot(self, steps: int, position: Position) -> bool:
        return position in self.open_spots[steps % len(self.open_spots)]
