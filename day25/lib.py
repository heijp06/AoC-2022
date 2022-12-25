def part1(rows: list[str]) -> int:
    return to_snafu(sum(from_snafu(row) for row in rows))


def part2(rows: list[str]) -> int:
    pass


def to_snafu(number: int) -> str:
    digits = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
    value = number
    snafu = ""
    while value > 0:
        value, rest = divmod(value, 5)
        if rest > 2:
            rest -= 5
            value += 1
        snafu = digits[rest] + snafu
    return snafu


def from_snafu(snafu: str) -> int:
    digits = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
    value = 0
    power = 1
    for digit in snafu[::-1]:
        value += digits[digit] * power
        power *= 5
    return value
