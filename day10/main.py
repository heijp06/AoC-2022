import pyperclip    # type: ignore
from lib import part1, part2


def read_rows():
    with open('data.txt', newline='') as csv_file:
        return csv_file.read().splitlines()


def clip(x):
    if x is None:
        return
    pyperclip.copy(x)


rows = list(read_rows())
x = part1(rows)
print(f"Part 1: {x}")
clip(x)

crt = part2(rows)
print("Part 2:")
for line in crt:
    print(line)
