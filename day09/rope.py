from collections import namedtuple


Vector = namedtuple("Vector", "x,y")


class Rope:
    def __init__(self, length: int) -> None:
        self.knots = [Vector(0, 0) for _ in range(length)]
        self.positions = {self.tail}

    @property
    def head(self) -> Vector:
        return self.knots[0]

    @property
    def tail(self) -> Vector:
        return self.knots[-1]

    @property
    def length(self) -> int:
        return len(self.knots)

    def up(self) -> None:
        self.move(Vector(0, 1))

    def down(self) -> None:
        self.move(Vector(0, -1))

    def left(self) -> None:
        self.move(Vector(-1, 0))

    def right(self) -> None:
        self.move(Vector(1, 0))

    def move(self, direction: Vector) -> None:
        self.knots[0] = Vector(self.head.x + direction.x,
                               self.head.y + direction.y)
        for i in range(1, self.length):
            head = self.knots[i - 1]
            tail = self.knots[i]
            delta = Vector(
                self.delta(head.x - tail.x, head.y - tail.y),
                self.delta(head.y - tail.y, head.x - tail.x)
            )
            self.knots[i] = Vector(tail.x + delta.x, tail.y + delta.y)
        self.positions.add(self.tail)

    def delta(self, delta_along: int, delta_across: int) -> int:
        if delta_along == 0:
            return 0
        if abs(delta_along) == 1 and abs(delta_across) < 2:
            return 0
        return delta_along // abs(delta_along)
