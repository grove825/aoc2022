from __future__ import annotations

import argparse
import os.path
from collections import defaultdict

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    elfs: dict[int, int] = defaultdict(int)
    elf = 1

    lines = s.splitlines()
    for line in lines:
        if line == "":
            elf += 1
            continue
        elfs[elf] = elfs[elf] + int(line)

    sorted_values = sorted(elfs, key=elfs.__getitem__, reverse=True)
    max_values = [elfs[i] for i in sorted_values]
    return sum(max_values[:3])


INPUT_S = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
EXPECTED = 45000


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
