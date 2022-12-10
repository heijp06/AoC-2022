def part1(rows: list[str]) -> int:
    trees = set()
    for row in range(len(rows)):
        for column in visible_trees(rows[row]):
            trees.add((row, column))
    transposed = transpose(rows)
    for column in range(len(transposed)):
        for row in visible_trees(transposed[column]):
            trees.add((row, column))
    return len(trees)


def part2(rows: list[str]) -> int:
    highest = 0
    for row in range(1, len(rows) - 1):
        for column in range(1, len(rows[0]) - 1):
            score = scenic_score(rows, (row, column))
            if score > highest:
                highest = score
    return highest


def transpose(rows: list[str]) -> list[str]:
    return list(map("".join, zip(*rows)))


def visible_trees(row: str) -> list[int]:
    height = -1
    visible = []
    for column in range(len(row)):
        if int(row[column]) > height:
            height = int(row[column])
            visible.append(column)
    height = -1
    for column in range(len(row) - 1, -1, -1):
        if int(row[column]) > height:
            height = int(row[column])
            visible.append(column)
    return visible


def scenic_score(rows: str, coordinates: tuple[int, int]) -> int:
    row, column = coordinates
    left, right = row_score(rows[row], column)
    transposed = transpose(rows)
    up, down = row_score(transposed[column], row)
    return left * right * up * down


def row_score(row: str, column: int) -> int:
    tree_height = int(row[column])
    left = 0
    for height in row[column - 1::-1]:
        left += 1
        if int(height) >= tree_height:
            break
    right = 0
    for height in row[column + 1:]:
        right += 1
        if int(height) >= tree_height:
            break
    return left, right
