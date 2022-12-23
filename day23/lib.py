from grid import parse


def part1(rows: list[str]) -> int:
    grid = parse(rows)
    grid.dump()
    for _ in range(3):
        grid.do_round()
        grid.dump()

    min_row = min(elve.row for elve in grid.elves)
    max_row = max(elve.row for elve in grid.elves)
    min_column = min(elve.column for elve in grid.elves)
    max_column = max(elve.column for elve in grid.elves)
    height = max_row - min_row + 1
    width = max_column - min_column + 1
    area = height * width

    return area - len(grid.elves)


def part2(rows: list[str]) -> int:
    pass
