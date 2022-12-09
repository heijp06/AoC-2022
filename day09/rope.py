from collections import namedtuple


Vector = namedtuple("Vector", "x,y")


class Rope:
    def __init__(self, length: int) -> None:
        self.segments = [Vector(0, 0) for _ in range(length)]
        self.positions = {self.tail}

    @property
    def head(self) -> Vector:
        return self.segments[0]

    @property
    def tail(self) -> Vector:
        return self.segments[-1]

    @property
    def length(self) -> int:
        return len(self.segments)

    def up(self) -> None:
        self.move(Vector(0, 1))

    def down(self) -> None:
        self.move(Vector(0, -1))

    def left(self) -> None:
        self.move(Vector(-1, 0))

    def right(self) -> None:
        self.move(Vector(1, 0))

    def move(self, direction: Vector) -> None:
        dx, dy = direction
        self.segments[0] = Vector(self.head.x + dx, self.head.y + dy)
        for i in range(1, self.length):
            head_x, head_y = self.segments[i - 1]
            tail_x, tail_y = self.segments[i]
            delta_x = self.delta(head_x - tail_x, head_y - tail_y)
            delta_y = self.delta(head_y - tail_y, head_x - tail_x)
            tail_x += delta_x
            tail_y += delta_y
            self.segments[i] = Vector(tail_x, tail_y)
        self.positions.add(self.tail)

    def delta(self, delta_along: int, delta_across: int) -> int:
        if delta_along == 0:
            return 0
        if abs(delta_along) == 1 and abs(delta_across) < 2:
            return 0
        return delta_along // abs(delta_along)
