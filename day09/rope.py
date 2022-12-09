from collections import namedtuple


Segment = namedtuple("Segment", "x,y")


class Rope:
    def __init__(self, length: int) -> None:
        self.segments = [Segment(0, 0) for _ in range(length)]

    def up():
        pass

    def down():
        pass

    def left():
        pass

    def right():
        pass
