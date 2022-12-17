from os import getcwd
from os.path import basename, dirname, join
import pyperclip    # type: ignore
from lib import part1, part2
from example import example


def read_row(**kwargs):
    with open(get_data_path(), encoding='ASCII', newline='') as csv_file:
        return csv_file.read().strip()


def get_data_path() -> str:
    path = getcwd()
    day = basename(path)
    return join(dirname(path), "data", f'{day}.txt')


def clip(data):
    if data is None:
        return
    pyperclip.copy(data)


row = read_row()
result1 = part1(row)
print(f"Part 1: {result1}")
clip(result1)

result2 = part2(row)
print(f"Part 2: {result2}")
clip(result2)
