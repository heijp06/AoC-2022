from collections import namedtuple
from functools import cmp_to_key
from ast import literal_eval
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
        left = literal_eval(rows[index])
        right = literal_eval(rows[index+1])
        pairs.append(Pair(left, right))
    return sum(
        index + 1 for index, pair in enumerate(pairs)
        if compare(pair.left, pair.right) == LT
    )


def part2(rows: list[str]) -> int:
    packets = [literal_eval(row) for row in rows if row]
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
    stack = []
    packet = None
    for token in re.findall(r"\[|]|\d+", row):
        match token:
            case "[":
                if packet is None:
                    packet = []
                    stack.append(packet)
                else:
                    new = []
                    stack[-1].append(new)
                    stack.append(new)
            case "]":
                stack.pop()
            case value:
                stack[-1].append(int(value))
    return packet


