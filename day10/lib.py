from device import Device


def part1(rows: list[str]) -> int:
    device = Device()
    device.execute(rows)
    return device.sum_of_signal_strengths


def part2(rows: list[str]) -> int:
    pass
