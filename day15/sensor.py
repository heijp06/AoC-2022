from __future__ import annotations
from collections import namedtuple
import re


Position = namedtuple("Position", "x,y")


def parse(row: str) -> Sensor:
    fields = re.findall(r"-?\d+", row)
    position = Position(int(fields[0]), int(fields[1]))
    beacon = Position(int(fields[2]), int(fields[3]))
    return Sensor(position, beacon)


class Sensor:
    def __init__(self, position: Position, beacon: Position):
        self.position = position
        self.beacon = beacon
        self.width = (abs(self.beacon.x - self.position.x) +
                      abs(self.beacon.y - self.position.y))

    def get_visible_columns(self, row: int) -> list[int]:
        width = self.width - abs(row - self.position.y)
        if width < 0:
            return []
        return list(range(self.position.x - width, self.position.x + width + 1))
    
    def __repr__(self) -> str:
        return f"{self.position}, {self.beacon}"
