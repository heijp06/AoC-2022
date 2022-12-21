from os import getcwd
from os.path import basename, dirname, join
import csv
import pyperclip    # type: ignore
from lib import part1, part2


def read_rows(**kwargs):
    with open(get_data_path(), encoding='ASCII', newline='') as csv_file:
        # return list(csv.reader(csv_file, **kwargs))
        # return csv_file.read().strip()
        return csv_file.read().splitlines()


def get_data_path() -> str:
    path = getcwd()
    day = basename(path)
    return join(dirname(path), "data", f'{day}.txt')


def clip(data):
    if data is None:
        return
    pyperclip.copy(data)


rows = [row for row in read_rows()]
result1 = part1(rows)
print(f"Part 1: {result1}")
clip(result1)

result2 = part2(rows)
print(f"Part 2: {result2}")
clip(result2)
