#!/usr/bin/env python3
# Generated by 2.6.0
# Copyright 2021 Yuichiro Smith
import sys


def solve(N: int, S: str):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == '__main__':
    main()