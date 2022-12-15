from sensor import Sensor, parse


def part1(rows: list[str], row_to_check: int = 2000000) -> int:
    sensors = [parse(row) for row in rows]
    return no_beacons(row_to_check, sensors)

def no_beacons(row: int, sensors: list[Sensor]):
    visible: set[int] = set()
    beacons_on_row: set[int] = set()
    for sensor in sensors:
        visible = visible.union(sensor.get_visible_columns(row))
        if sensor.beacon.y == row:
            beacons_on_row.add(sensor.beacon.x)
    return len(visible) - len(beacons_on_row)


def part2(rows: list[str], size: int = 4000000) -> int:
    pass
