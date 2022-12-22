from board import parse


def part1(rows: list[str]) -> int:
    board = parse(rows)
    board.go(1)
    return board.password()

def part2(rows: list[str]) -> int:
    board = parse(rows)
    board.go(2)
    return board.password()
