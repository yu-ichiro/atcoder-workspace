#!/usr/bin/env python3
# Generated by AtCoder Tools 2.8.0
# Copyright 2021 Yuichiro Smith
import sys


def solve(N: int, A: "List[int]", u: "List[int]", v: "List[int]"):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, A, u, v)


if __name__ == '__main__':
    main()
