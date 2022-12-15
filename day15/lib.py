from sensor import Sensor, parse

from collections import namedtuple

Section = namedtuple("Section", "start, end")


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
    sensors = [parse(row) for row in rows]
    for y in range(size + 1):
        sections: list[Section] = []
        for sensor in sensors:
            length = sensor.width - abs(sensor.position.y - y)
            if length < 0:
                continue
            start_x = max(0, sensor.position.x - length)
            end_x = min(size, sensor.position.x + length)
            section = Section(start_x, end_x)
            new_sections = []
            for other in sections:
                if (section.start <= other.start <= section.end or section.start <= other.end <= section.end or 
                    other.start <= section.start <= other.end or other.start <= section.end <= other.end):
                    section = Section(
                        min(section.start, other.start), max(section.end, other.end))
                else:
                    new_sections.append(other)
            new_sections.append(section)
            sections = new_sections
        if sections != [Section(0, size)]:
            if len(sections) == 1:
                x = 0 if sections[0].start != 0 else size
            else:
                sections.sort()
                x = sections[0].end + 1
            return 4000000 * x + y