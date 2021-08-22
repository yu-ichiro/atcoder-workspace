#!/usr/bin/env python3
# Generated by AtCoder Tools 2.8.0
# Copyright 2021 Yuichiro Smith
import sys

MOD = 998244353  # type: int


def solve(N: int):
    if N == 1:
        print(1)
        return
    ans = 0
    for i in range(1, N):
        if i * i > N:
            break
        ans += (N - i*i) // (2 * i) + 1
        ans %= MOD
    print(ans % MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()