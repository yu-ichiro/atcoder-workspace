#!/usr/bin/env python3
# Generated by AtCoder Tools 2.8.0
# Copyright 2021 Yuichiro Smith
import sys


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, A, B, C)


if __name__ == '__main__':
    main()
