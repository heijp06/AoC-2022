scores1 = {
    "A X": 4,  # R R -> D, 1 + 3 = 4
    "A Y": 8,  # R P -> W, 2 + 6 = 8
    "A Z": 3,  # R S -> L, 3 + 0 = 3

    "B X": 1,  # P R -> L, 1 + 0 = 1
    "B Y": 5,  # P P -> D, 2 + 3 = 5
    "B Z": 9,  # P S -> W, 3 + 6 = 9

    "C X": 7,  # S R -> W, 1 + 6 = 7
    "C Y": 2,  # S P -> L, 2 + 0 = 2
    "C Z": 6,  # S S -> D, 3 + 3 = 6

    "": 0,  # Empty line at the end.
}

scores2 = {
    "A X": 3,  # R L -> S, 3 + 0 = 3
    "A Y": 4,  # R D -> R, 1 + 3 = 4
    "A Z": 8,  # R W -> P, 2 + 6 = 8

    "B X": 1,  # P L -> R, 1 + 0 = 1
    "B Y": 5,  # P D -> P, 2 + 3 = 5
    "B Z": 9,  # P W -> S, 3 + 6 = 9

    "C X": 2,  # S L -> P, 2 + 0 = 2
    "C Y": 6,  # S D -> S, 3 + 3 = 6
    "C Z": 7,  # S W -> R, 1 + 6 = 7

    "": 0,  # Empty line at the end.
}


def part1(rows: list[str]) -> int:
    return sum(get_rounds1(rows))


def part2(rows: list[str]) -> int:
    return sum(get_rounds2(rows))


def get_rounds1(rows: list[str]) -> list[int]:
    return [scores1[row] for row in rows]


def get_rounds2(rows: list[str]) -> list[int]:
    return [scores2[row] for row in rows]
