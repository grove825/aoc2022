from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    rtn_val: int = 0
    shape_map: dict[str, str] = {
        "A": "Rock",
        "X": "Rock",
        "B": "Paper",
        "Y": "Paper",
        "C": "Scissors",
        "Z": "Scissors",
    }
    shape_val: dict[str, int] = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
    }
    win = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    lines = s.splitlines()
    for line in lines:
        play1, play2 = line.split(" ")
        player1 = shape_map.get(play1)
        player2 = shape_map.get(play2)
        rtn_val += shape_val.get(player2)
        if player1 == player2:
            rtn_val += 3
        elif win[player1] != player2:
            rtn_val += 6
        else:
            pass

    return rtn_val


INPUT_S = """\
A Y
B X
C Z
"""
EXPECTED = 15


INPUT_S = """\
A Z
C Z
A Z
"""
EXPECTED = 1 + 1 + 3 + 0 + 3 + 0


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
