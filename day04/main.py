import pyperclip    # type: ignore
from lib import part1, part2


def read_rows(**kwargs):
    with open('..\\data\\day04\\data.txt', newline='') as csv_file:
        return csv_file.read().splitlines()


def clip(x):
    if x is None:
        return
    pyperclip.copy(x)


rows = list(read_rows())
x = part1(rows)
print(f"Part 1: {x}")
clip(x)

x = part2(rows)
print(f"Part 2: {x}")
clip(x)
