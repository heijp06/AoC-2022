import pyperclip    # type: ignore
from lib import part1, part2


def read_data():
    with open('..\\data\\day06\\data.txt', newline='') as csv_file:
        return csv_file.read().strip()


def clip(x):
    if x is None:
        return
    pyperclip.copy(x)


data = read_data()
x = part1(data)
print(f"Part 1: {x}")
clip(x)

x = part2(data)
print(f"Part 2: {x}")
clip(x)
