from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    rtn_val = 0
    lines = s.splitlines()
    for line in lines:
        elf1, elf2 = line.split(",")
        section1 = [i for i in range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1)]
        section2 = [i for i in range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1)]
        check1 = [False if i not in section2 else True for i in section1]
        check2 = [False if i not in section1 else True for i in section2]
        if all(check1) or all(check2):
            rtn_val +=1

    return rtn_val


INPUT_S = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
EXPECTED = 2


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
