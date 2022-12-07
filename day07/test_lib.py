import pytest
from lib import part1, part2
from tree_parser import TreeParser


def test_part1():
    assert part1(rows) == 95437


def test_part2():
    assert part2(rows) == 24933642


def test_parse():
    parser = TreeParser(rows)
    root = parser.parse()
    assert root


rows = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]
