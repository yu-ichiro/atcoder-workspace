#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[int]", T: "List[int]"):
    R = [t for t in T]
    update = True
    while update:
        update = False
        for i in enumerate(range(N)):
            idx = i % N
            nxt = (idx+1) % N
            pass_t = R[idx] + S[idx]
            if R[nxt] > pass_t:
                R[nxt] = pass_t
                update = True
    for r in R:
        print(r)

    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, S, T)

if __name__ == '__main__':
    main()
