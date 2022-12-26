import functools
import itertools


digits = ["=", "-", "0", "1", "2"]


def part1(rows: list[str]) -> str:
    return functools.reduce(add, rows, "0")


def add(snafu1: str, snafu2: str) -> str:
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
