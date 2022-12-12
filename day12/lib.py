Grid = list[list[int]]
Vector = tuple[int, int]

def part1(rows: list[str]) -> int:
    start, end, grid = parse(rows)
    positions = [(0, 0)]
    seen = {(0, 0)}
    step = 0
    while True:
        for row, column in positions:
            for drow, dcolumn in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_position = row + drow, column + dcolumn
                if new_position in seen:
                    continue


def part2(rows: list[str]) -> int:
    pass


def parse(rows: list[str]) -> tuple[Vector, Vector, Grid]:
    grid: Grid = []
    start = -1
    end = -1
    for row in range(len(rows)):
        line: list[int] = []
        grid.append(line)
        for column in range(len(rows[0])):
            letter = rows[row][column]
            if letter == 'S':
                line.append(0)
                start = row, column
            elif letter == 'E':
                line.append(25)
                end = row, column
            else:
                line.append(ord(letter) - ord('a'))
    return start, end, grid