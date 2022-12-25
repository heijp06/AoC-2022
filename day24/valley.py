from __future__ import annotations
import itertools
from queue import PriorityQueue
from typing import NamedTuple, Optional


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
    targets: tuple[Position, ...]


class Valley:  # pylint: disable=too-many-instance-attributes
    def __init__(self, rows: list[str]) -> None:
        self.height = len(rows)
        self.width = len(rows[0])
        self.grid = rows
        self.start = Position(0, 1)
        self.end = Position(self.height - 1, self.width - 2)
        self.states: PriorityQueue = PriorityQueue()
        self.seen: set[State] = set()
        self.min_distance: Optional[int] = None
        self.min_path_length = self.manhattan_distance(self.start, self.end)

    def solve(self, part: int) -> None:
        self.seen.clear()
        if part == 1:
            start_state = State(0, self.start, (self.end,))
        elif part == 2:
            start_state = State(
                0, self.start, (self.end, self.start, self.end))
        else:
            raise ValueError(f"part == {part}, should be 1 or 2.")
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
        self.seen.add(state)
        self.states.put((self.get_min_distance(state), state))

    def get_min_distance(self, state: State) -> int:
        to_target = self.manhattan_distance(state.position, state.targets[0])
        rest = (len(state.targets) - 1) * self.min_path_length
        return state.steps + to_target + rest

    def manhattan_distance(self, position1: Position, position2: Position) -> int:
        return abs(position2.row - position1.row) + abs(position2.column - position1.column)

    def create_new_states(self, state: State) -> None:
        for direction in itertools.starmap(Position, [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]):
            new_steps = state.steps + 1
            new_position = state.position + direction
            new_targets = state.targets
            if not self.is_open_spot(new_steps, new_position):
                continue
            if new_position == state.targets[0]:
                if len(state.targets) == 1:
                    self.min_distance = min(
                        self.min_distance or new_steps, new_steps)
                    return
                new_targets = state.targets[1:]
            self.add_state(State(new_steps, new_position, new_targets))

    def is_open_spot(self, steps: int, position: Position) -> bool:
        if position in (self.start, self.end):
            return True
        if (position.row <= 0 or position.row >= self.height - 1
                or position.column <= 0 or position.column >= self.width - 1):
            return False
        return (
            self.check(steps, position, ">") and
            self.check(steps, position, "v") and
            self.check(steps, position, "<") and
            self.check(steps, position, "^")
        )

    def check(self, steps: int, position: Position, blizzard: str) -> bool:
        match blizzard:
            case ">":
                length = self.width - 2
                column = (position.column - 1 - steps) % length + 1
                return self.grid[position.row][column] != blizzard
            case "v":
                length = self.height - 2
                row = (position.row - 1 - steps) % length + 1
                return self.grid[row][position.column] != blizzard
            case "<":
                length = self.width - 2
                column = (position.column - 1 + steps) % length + 1
                return self.grid[position.row][column] != blizzard
            case "^":
                length = self.height - 2
                row = (position.row - 1 + steps) % length + 1
                return self.grid[row][position.column] != blizzard
        raise ValueError(f"Unexpected blizzard '{blizzard}'")
