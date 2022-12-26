import functools
import itertools


digits = ["=", "-", "0", "1", "2"]
SNAFU = str


def part1(rows: list[SNAFU]) -> SNAFU:
    return functools.reduce(add, rows, "0")


def add(snafu1: SNAFU, snafu2: SNAFU) -> SNAFU:
    result = ""
    carry = 0
    for digit1, digit2 in itertools.zip_longest(snafu1[::-1], snafu2[::-1], fillvalue="0"):
        digit = digits.index(digit1) + digits.index(digit2) + carry - 4
        if digit < -2:
            digit += 5
            carry = -1
        elif digit > 2:
            digit -= 5
            carry = 1
        else:
            carry = 0
        result = digits[digit + 2] + result
    if carry == -1:
        result = f"-{result}"
    elif carry == 1:
        result = f"1{result}"
    return result
