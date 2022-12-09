Vector = tuple[int, int]


def part1(rows: list[str]) -> int:
    head_pos = 0, 0
    tail_pos = 0, 0
    positions: set[Vector] = {tail_pos}
    for row in rows:
        fields = row.split()
        count = int(fields[1])
        match fields[0]:
            case 'R':
                head_pos, tail_pos = move(
                    (1, 0), count, head_pos, tail_pos, positions)
            case 'U':
                head_pos, tail_pos = move(
                    (0, 1), count, head_pos, tail_pos, positions)
            case 'L':
                head_pos, tail_pos = move(
                    (-1, 0), count, head_pos, tail_pos, positions)
            case 'D':
                head_pos, tail_pos = move(
                    (0, -1), count, head_pos, tail_pos, positions)
    return len(positions)


def part2(rows: list[str]) -> int:
    pass


def move(
        direction: Vector,
        count: int,
        head_pos: Vector,
        tail_pos: Vector,
        positions: set[Vector]) -> tuple[Vector, Vector]:
    direction_x, direction_y = direction
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos
    for _ in range(count):
        head_x += direction_x
        head_y += direction_y
        delta_x = delta(head_x - tail_x, abs(head_y - tail_y))
        delta_y = delta(head_y - tail_y, abs(head_x - tail_x))
        tail_x += delta_x
        tail_y += delta_y
        positions.add((tail_x, tail_y))
    return (head_x, head_y), (tail_x, tail_y)


def delta(delta_along: int, abs_delta_across: int) -> int:
    if delta_along == 0:
        return 0
    if abs(delta_along) == 1 and abs_delta_across < 2:
        return 0
    return delta_along // abs(delta_along)
