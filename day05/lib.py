import re
from typing import Callable, NamedTuple


class Step(NamedTuple):
    repeat: int
    start: int
    end: int


Stack = list[str]
CraneOperation = Callable[[list[Stack], Step], None]


def part1(rows: list[str]) -> str:
    return rearrange(rows, crate_mover_9000)


def part2(rows: list[str]) -> str:
    return rearrange(rows, crate_mover_9001)


def rearrange(rows: list[str], crane_operation: CraneOperation) -> str:
    stacks = parse_stacks(rows)
    steps = parse_steps(rows)
    for step in steps:
        crane_operation(stacks, step)
    return "".join(stack[-1] for stack in stacks)


def crate_mover_9000(stacks: list[Stack], step: Step) -> None:
    for _ in range(step.repeat):
        crate = stacks[step.start - 1].pop()
        stacks[step.end - 1].append(crate)


def crate_mover_9001(stacks: list[Stack], step: Step) -> None:
    stacks[step.end - 1] += stacks[step.start - 1][-step.repeat:]
    stacks[step.start - 1] = stacks[step.start - 1][:-step.repeat]


def parse_stacks(rows: list[str]) -> list[Stack]:
    number_of_stacks = len(rows[0]) // 4 + 1
    stacks: list[Stack] = [[] for _ in range(number_of_stacks)]
    for row in rows:
        if row[1] == "1":
            return stacks
        for i in range(number_of_stacks):
            index = 4 * i + 1
            if row[index] != " ":
                stacks[i].insert(0, row[index])
    raise ValueError(rows)


def parse_steps(rows: list[str]) -> list[Step]:
    steps = []
    for row in rows:
        if match := re.match("move (\d*) from (\d) to (\d)", row):
            repeat, start, end = match.groups()
            steps.append(Step(int(repeat), int(start), int(end)))
    return steps
