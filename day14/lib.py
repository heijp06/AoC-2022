from cave import Cave, Point, parse


def part1(rows: list[str]) -> int:
    cave = parse(rows)
    count = 0
    while True:
        sand = cave.start
        while sand.y < cave.y_max:
            new_sand = fall(sand, cave)
            if new_sand == sand:
                cave.stuff.add(sand)
                count += 1
                break
            sand = new_sand
        if sand.y >= cave.y_max:
            return count


def part2(rows: list[str]) -> int:
    pass


def fall(sand: Point, cave: Cave) -> Point:
    for delta in [0, -1, 1]:
        new_sand = Point(sand.x + delta, sand.y + 1)
        if new_sand not in cave.stuff:
            return new_sand
    return sand
