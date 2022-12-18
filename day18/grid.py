from shapes import Cube, Point


class Grid:
    def __init__(self, cubes: list[Cube]) -> None:
        self.lava = set(cubes)
        self.outside_air: set[Cube] = set()
        self.trapped_air: set[Cube] = set()
        self.set_min_max()

    def set_min_max(self):
        min_x = min(cube.offset.x for cube in self.lava)
        min_y = min(cube.offset.y for cube in self.lava)
        min_z = min(cube.offset.z for cube in self.lava)
        max_x = max(cube.offset.x for cube in self.lava)
        max_y = max(cube.offset.y for cube in self.lava)
        max_z = max(cube.offset.z for cube in self.lava)
        self.minimum = Point(min_x, min_y, min_z)
        self.maximum = Point(max_x, max_y, max_z)

    def find_trapped_air(self) -> None:
        self.create_border()
        for x in range(self.minimum.x, self.maximum.x + 1):
            for y in range(self.minimum.y, self.maximum.y + 1):
                for z in range(self.minimum.z, self.maximum.z + 1):
                    cube = Cube(Point(x, y, z))
                    if cube in self.lava:
                        continue
                    if cube in self.outside_air:
                        continue
                    if cube in self.trapped_air:
                        continue
                    self.assign(cube)

    def assign(self, unknown: Cube) -> None:
        unknowns = {unknown}
        cubes = [unknown]
        while cubes:
            new_cubes: list[Cube] = []
            for cube in cubes:
                neighbours = [Cube(cube.offset + offset) for offset in [
                    Point(1, 0, 0), Point(-1, 0, 0),
                    Point(0, 1, 0), Point(0, -1, 0),
                    Point(0, 0, 1), Point(0, 0, -1)
                ]]
                for neighbour in neighbours:
                    if neighbour in unknowns:
                        continue
                    if neighbour in self.lava:
                        continue
                    if neighbour in self.trapped_air:
                        self.trapped_air |= unknowns
                        return
                    if neighbour in self.outside_air:
                        self.outside_air |= unknowns
                        return
                    unknowns.add(neighbour)
                    new_cubes.append(neighbour)
                cubes = new_cubes
        self.trapped_air |= unknowns

    def create_border(self) -> None:
        self.outside_air |= {
            Cube(Point(self.minimum.x - 1, y, z))
            for y in range(self.minimum.y - 1, self.maximum.y + 2)
            for z in range(self.minimum.z - 1, self.maximum.z + 2)
        }
        self.outside_air |= {
            Cube(Point(self.maximum.x + 1, y, z))
            for y in range(self.minimum.y - 1, self.maximum.y + 2)
            for z in range(self.minimum.z - 1, self.maximum.z + 2)
        }
        self.outside_air |= {
            Cube(Point(x, self.minimum.y - 1, z))
            for x in range(self.minimum.x - 1, self.maximum.x + 2)
            for z in range(self.minimum.z - 1, self.maximum.z + 2)
        }
        self.outside_air |= {
            Cube(Point(x, self.maximum.y + 1, z))
            for x in range(self.minimum.x - 1, self.maximum.x + 2)
            for z in range(self.minimum.z - 1, self.maximum.z + 2)
        }
        self.outside_air |= {
            Cube(Point(x, y, self.minimum.z - 1))
            for x in range(self.minimum.x - 1, self.maximum.x + 2)
            for y in range(self.minimum.y - 1, self.maximum.y + 2)
        }
        self.outside_air |= {
            Cube(Point(x, y, self.maximum.z + 1))
            for x in range(self.minimum.x - 1, self.maximum.x + 2)
            for y in range(self.minimum.y - 1, self.maximum.y + 2)
        }
