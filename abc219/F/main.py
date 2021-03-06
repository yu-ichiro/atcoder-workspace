#!/usr/bin/env python3
# Generated by AtCoder Tools 2.8.0
# Copyright 2021 Yuichiro Smith
import sys
from collections import defaultdict


def solve(S: str, K: int):
    dx, dy = 0, 0
    max_x, max_y = 0, 0
    cleansed_grid = {(0, 0): K}
    for s in S:
        if s == "R":
            dx += 1
            max_x = max(max_x, dx)
        if s == "L":
            dx -= 1
        if s == "D":
            dy += 1
            max_y = max(max_y, dy)
        if s == "U":
            dy -= 1
        cleansed_grid[(dx, dy)] = K
    if dx == 0 and dy == 0:
        return print(len(cleansed_grid))
    group_by_y = dx == 0
    groups = defaultdict(list)
    if group_by_y:
        dx, dy = dy, dx
    for x, y in cleansed_grid:
        if group_by_y:
            x, y = y, x
        q, s = divmod(x, dx)
        t = y - dy*q
        groups[(s, t)].append((q, x, y))
    # print(groups)
    for pairs in groups.values():
        if len(pairs) == 1:
            continue
        pairs.sort()
        for (q1, _, _), (q2, x2, y2) in zip(pairs, pairs[1:]):
            if group_by_y:
                x2, y2 = y2, x2
            if cleansed_grid[(x2, y2)] > q2 - q1:
                cleansed_grid[(x2, y2)] = q2 - q1
    # print(cleansed_grid)
    print(sum(v for v in cleansed_grid.values()))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(S, K)


if __name__ == '__main__':
    main()
