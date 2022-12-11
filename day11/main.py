import csv
import pyperclip    # type: ignore
from os import getcwd
from os.path import basename, dirname, join
from lib import part1, part2


def read_rows(**kwargs):
    with open(get_data_path(), newline='') as csv_file:
        # return list(csv.reader(csv_file, **kwargs))
        # return csv_file.read().strip()
        return csv_file.read().splitlines()


def get_data_path() -> str:
    path = getcwd()
    day = basename(path)
    return join(dirname(path), "data", f'{day}.txt')


def clip(x):
    if x is None:
        return
    pyperclip.copy(x)


rows = [row for row in read_rows()]
x = part1(rows)
print(f"Part 1: {x}")
clip(x)

x = part2(rows)
print(f"Part 2: {x}")
clip(x)
