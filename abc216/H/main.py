#!/usr/bin/env python3
# Generated by AtCoder Tools 2.8.0
# Copyright 2021 Yuichiro Smith
import sys

MOD = 998244353  # type: int


def solve(K: int, N: int, x: "List[int]"):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(K, N, x)


if __name__ == '__main__':
    main()
