import re
from typing import NamedTuple

Stack = list[str]


class Step(NamedTuple):
    repeat: int
    start: int
    end: int


def part1(rows: list[str]) -> int:
    stacks = parse_stacks(rows)
    steps = parse_steps(rows)
    for step in steps:
        for _ in range(step.repeat):
            crate = stacks[step.start - 1].pop()
            stacks[step.end - 1].append(crate)
    return "".join(stack[-1] for stack in stacks)


def part2(rows: list[str]) -> int:
    pass


def parse_stacks(rows: list[str]) -> list[Stack]:
    number_of_stacks = len(rows[0]) // 4 + 1
    stacks = [[] for _ in range(number_of_stacks)]
    for row in rows:
        if row[1] == "1":
            return stacks
        for i in range(number_of_stacks):
            index = 4 * i + 1
            if row[index] != " ":
                stacks[i].insert(0, row[index])


def parse_steps(rows: list[str]) -> list[Step]:
    steps = []
    for row in rows:
        if row and row[0] == "m":
            repeat, start, end = re.match(
                "move (\d*) from (\d) to (\d)", row).groups()
            steps.append(Step(int(repeat), int(start), int(end)))
    return steps
