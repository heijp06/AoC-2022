from board import parse


def part1(rows: list[str]) -> int:
    board = parse(rows)
    board.go()
    return board.password()

def part2(rows: list[str]) -> int:
    pass
