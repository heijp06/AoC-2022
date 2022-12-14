import ast

import pytest
from lib import Packet, parse, part1, part2
from example import rows, RESULT1, RESULT2


def test_part1():
    assert part1(rows) == RESULT1


def test_part2():
    assert part2(rows) == RESULT2


@pytest.mark.parametrize("row,packet", [(row, ast.literal_eval(row)) for row in rows if row])
def test_parse(row: str, packet: Packet) -> None:
    assert parse(row) == packet
