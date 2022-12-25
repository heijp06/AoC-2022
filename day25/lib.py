digits = ((-2, "="), (-1, "-"), (0, "0"), (1, "1"), (2, "2"))


def part1(rows: list[str]) -> str:
    return to_snafu(sum(from_snafu(row) for row in rows))


def to_snafu(number: int) -> str:
    value = number
    snafu = ""
    while value > 0:
        value, rest = divmod(value, 5)
        if rest > 2:
            rest -= 5
            value += 1
        snafu = to_digit(rest) + snafu
    return snafu


def from_snafu(snafu: str) -> int:
    value = 0
    power = 1
    for digit in snafu[::-1]:
        value += from_digit(digit) * power
        power *= 5
    return value


def to_digit(number: int) -> str:
    for value, representation in digits:
        if number == value:
            return representation
    raise ValueError(f"{number} cannot be represented as a single SNAFU digit.")


def from_digit(digit: str) -> int:
    for value, representation in digits:
        if digit == representation:
            return value
    raise ValueError(f"Unknown SNAFU digit {digit}.")
