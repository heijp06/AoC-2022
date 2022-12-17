from tower import Tower


def part1(jets: str) -> int:
    tower = Tower(jets)
    for _ in range(2022):
        tower.drop_rock()
    return tower.height


def part2(jets: str) -> int:
    pass
