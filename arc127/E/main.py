#!/usr/bin/env python3
# Generated by AtCoder Tools 2.8.0
# Copyright 2021 Yuichiro Smith
import sys

MOD = 998244353  # type: int


def solve(A: int, B: int, X: "List[int]"):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(A + B)]  # type: "List[int]"
    solve(A, B, X)


if __name__ == '__main__':
    main()
