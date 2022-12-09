from rope import Rope


def part1(rows: list[str]) -> int:
    return move_rope(rows, 2)


def part2(rows: list[str]) -> int:
    return move_rope(rows, 10)


def move_rope(rows, length: int = 2) -> int:
    rope = Rope(length)
    steps = {'R': rope.right, 'U': rope.up, 'L': rope.left, 'D': rope.down}
    for row in rows:
        fields = row.split()
        step = steps[fields[0]]
        count = int(fields[1])
        for _ in range(count):
            step()
    return len(rope.positions)
