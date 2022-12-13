from collections import namedtuple
from functools import cmp_to_key

LT = -1
EQ = 0
GT = 1

Pair = namedtuple("Pair", "left,right")


def part1(rows: list[str]) -> int:
    pairs = parse(rows)
    count = 0
    for index, pair in enumerate(pairs):
        if compare(pair.left, pair.right) == LT:
            count += index + 1
    return count


def part2(rows: list[str]) -> int:
    packets = [eval(row) for row in rows if row]
    packets += [[[2]], [[6]]]
    packets.sort(key = cmp_to_key(compare))
    index1 = 1 + packets.index([[2]])
    index2 = 1 + packets.index([[6]])
    return index1 * index2


def parse(rows: list[str]) -> list[Pair]:
    pairs: list[Pair] = []
    for index in range(0, len(rows), 3):
        left = eval(rows[index])
        right = eval(rows[index+1])
        pairs.append(Pair(left, right))
    return pairs


def compare(left, right) -> int:
    if left == right:
        return EQ
    if isinstance(left, int):
        if isinstance(right, int):
            return LT if left < right else GT
        return compare([left], right)
    if isinstance(right, int):
        return compare(left, [right])
    if not left:
        return LT if right else EQ
    if not right:
        return GT
    result = compare(left[0], right[0])
    return compare(left[1:], right[1:]) if result == EQ else result
