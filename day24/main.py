import datetime
from os import getcwd
from os.path import basename, dirname, join
import pyperclip    # type: ignore
from lib import part1, part2


def read_rows():
    with open(get_data_path(), encoding='ASCII', newline='') as csv_file:
        return csv_file.read().splitlines()


def get_data_path() -> str:
    path = getcwd()
    day = basename(path)
    return join(dirname(path), "data", f'{day}.txt')


def clip(data):
    if data is None:
        return
    pyperclip.copy(data)


rows = list(read_rows())
t0 = datetime.datetime.now()
result1 = part1(rows)
t1 = datetime.datetime.now()
print(f"Part 1: {result1}")
clip(result1)

t2 = datetime.datetime.now()
result2 = part2(rows)
t3 = datetime.datetime.now()
print(f"Part 2: {result2}")
clip(result2)

print(t1 - t0)
print(t3 - t2)
print(t1 - t0 + t3 - t2)
