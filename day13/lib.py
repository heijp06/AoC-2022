from collections import namedtuple
from functools import cmp_to_key
import re
from typing import Any, Union

LT = -1
EQ = 0
GT = 1

Pair = namedtuple("Pair", "left,right")
Packet = Union[int, list[Any]]


def part1(rows: list[str]) -> int:
    pairs: list[Pair] = []
    for index in range(0, len(rows), 3):
        left = parse(rows[index])
        right = parse(rows[index+1])
        pairs.append(Pair(left, right))
    return sum(
        index + 1 for index, pair in enumerate(pairs)
        if compare(pair.left, pair.right) == LT
    )


def part2(rows: list[str]) -> int:
    packets = [parse(row) for row in rows if row]
    divider_packet1 = [[2]]
    divider_packet2 = [[6]]
    packets += [divider_packet1, divider_packet2]
    packets.sort(key=cmp_to_key(compare))
    return (packets.index(divider_packet1) + 1) * (packets.index(divider_packet2) + 1)


def compare(left: Packet, right: Packet) -> int:
    if left == right:
        return EQ
    if isinstance(left, int):
        if isinstance(right, int):
            return LT if left < right else GT
        return compare([left], right)
    if isinstance(right, int):
        return compare(left, [right])
    if left and right:
        result = compare(left[0], right[0])
        return compare(left[1:], right[1:]) if result == EQ else result
    return GT if left else LT


def parse(row: str) -> Packet:
    stack: list[list[Any]] = [[]]
    for token in re.findall(r"\[|]|\d+", row)[1:-1]:
        match token:
            case "[":
                packet: list[Packet] = []
                stack[-1].append(packet)
                stack.append(packet)
            case "]":
                stack.pop()
            case value:
                stack[-1].append(int(value))
    return stack[0]
