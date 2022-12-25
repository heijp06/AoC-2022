digits = ["=", "-", "0", "1", "2"]


def part1(rows: list[str]) -> str:
    return to_snafu(sum(from_snafu(row) for row in rows))


def to_snafu(number: int) -> str:
    value = number
    snafu = ""
    while value > 0:
        value, digit = divmod(value, 5)
        if digit > 2:
            digit -= 5
            value += 1
        snafu = digits[digit + 2] + snafu
    return snafu


def from_snafu(snafu: str) -> int:
    value = 0
    power = 1
    for digit in snafu[::-1]:
        value += (digits.index(digit) - 2) * power
        power *= 5
    return value
