#!/usr/bin/env python3
# Generated by AtCoder Tools 2.8.0
# Copyright 2021 Yuichiro Smith
import sys


def solve(S: "List[str]", T: int):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = [next(tokens) for _ in range(3)]  # type: "List[str]"
    T = int(next(tokens))  # type: int
    solve(S, T)


if __name__ == '__main__':
    main()