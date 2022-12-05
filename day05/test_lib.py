from lib import Step, parse_stacks, parse_steps, part1, part2


def test_part1():
    assert part1(rows) == "CMZ"


def test_part2():
    assert part2(rows) == "MCD"


def test_parse_stacks():
    assert parse_stacks(rows) == [
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"],
    ]


def test_parse_steps():
    assert parse_steps(rows) == [
        Step(1, 2, 1),
        Step(3, 1, 3),
        Step(2, 2, 1),
        Step(1, 1, 2)
    ]


rows = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2"
]
