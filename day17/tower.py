from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


Rock = set[Point]


class Tower:
    WIDTH = 7

    def __init__(self, jets: str) -> None:
        self.jets = jets
        self.current_jet = 0
        self.create_rocks()
        self.current_rock = 0
        self.height = 0
        self.tower = {Point(x, 0) for x in range(Tower.WIDTH)}  # the floor

    def create_rocks(self) -> None:
        self.rocks = [
            {Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)},
            {Point(1, 0), Point(0, 1), Point(1, 1), Point(2, 1), Point(1, 2)},
            {Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1), Point(2, 2)},
            {Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)},
            {Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)}
        ]

    def drop_rock(self) -> None:
        y = self.height + 4
        x = 3
        rock = self.get_rock(x, y)
        # self.draw(rock)
        while True:
            new_rock = self.push(rock)
            # self.draw(new_rock)
            rock = new_rock
            new_rock = self.drop(rock)
            # self.draw(new_rock)
            if rock == new_rock:
                break
            rock = new_rock
        self.tower |= rock
        self.height = max(point.y for point in self.tower)
            

    def get_rock(self, x: int, y: int) -> Rock:
        rock = self.rocks[self.current_rock]
        self.current_rock = (self.current_rock + 1) % len(self.rocks)
        return self.move_rock(x, y, rock)

    def move_rock(self, x: int, y: int, rock: Rock) -> Rock:
        return {Point(point.x + x, point.y + y) for point in rock}

    def push(self, rock: Rock) -> Rock:
        jet = self.jets[self.current_jet]
        self.current_jet = (self.current_jet + 1) % len(self.jets)
        direction = -1 if jet == "<" else 1
        new_rock = self.move_rock(direction, 0, rock)
        if new_rock & self.tower:
            return rock
        if any(point.x <= 0 or point.x > Tower.WIDTH for point in new_rock):
            return rock
        return new_rock
    
    def drop(self, rock: Rock) -> Rock:
        new_rock = self.move_rock(0, -1, rock)
        return rock if new_rock & self.tower else new_rock
    
    def draw(self, rock: Rock) -> None:
        height = max(point.y for point in rock)
        for y in range(height, 0, -1):
            line = "|"
            for x in range(1, Tower.WIDTH + 1):
                point = Point(x, y)
                if point in rock:
                    line += "@"
                elif point in self.tower:
                    line += "#"
                else:
                    line += "."
            line += "|"
            print(line)
        print("+" + "-" * Tower.WIDTH + "+")
        print()
