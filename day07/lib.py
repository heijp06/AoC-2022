from file_system import Directory
from tree_parser import TreeParser


def part1(rows: list[str]) -> int:
    parser = TreeParser(rows)
    root = parser.parse()
    sizes = {}
    get_sizes(root, sizes, "")
    return sum(size for size in sizes.values() if size <= 100000)


def part2(rows: list[str]) -> int:
    parser = TreeParser(rows)
    root = parser.parse()
    sizes = {}
    get_sizes(root, sizes, "")
    total_space = 70000000
    needed = 30000000
    used = sizes["/"]
    unused = total_space - used
    free_up = needed - unused
    return min(size for size in sizes.values() if size >= free_up)


def get_sizes(directory: Directory, sizes: dict[str, int], path: str) -> int:
    new_path = f"{path}/{directory.name}"
    sizes[new_path] = directory.get_size()
    for entry in directory.entries:
        if isinstance(entry, Directory):
            get_sizes(entry, sizes, new_path)

