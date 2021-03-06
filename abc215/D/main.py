#!/usr/bin/env python3
# Generated by 2.6.0
# Copyright 2021 Yuichiro Smith
import sys

sys.setrecursionlimit(10**9)


def factors(N):
    result = []
    n = 2
    while n * n <= N:
        if N % n != 0:
            n += 1
            continue
        while N % n == 0:
            N //= n
            result.append(n)
        n += 1
    if N != 1:
        result.append(N)
    return result


def solve(_N: int, M: int, A: "List[int]"):
    result = list(range(M+1))
    for a in set(A):
        for factor in factors(a):
            if M < factor or not result[factor]:
                continue
            for i in range(factor, M+1, factor):
                result[i] = 0
    result = [f for f in result if f]
    print(len(result))
    for answer in result:
        print(answer)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == '__main__':
    main()
