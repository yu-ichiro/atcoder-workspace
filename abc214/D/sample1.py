import sys
sys.setrecursionlimit(10**9)
def root(x):
    if rank[x] < 0: return x
    rank[x] = root(rank[x])
    return rank[x]
def unite(x, y):
    x, y = root(x), root(y)
    if x == y: return False
    if rank[x] > rank[y]: x, y = y, x
    rank[x] += rank[y]
    rank[y] = x
    return True
def is_same(x, y): return root(x) == root(y)
def size(x): return -rank[root(x)]
 
n = int(input())
uvw = [tuple(map(int, input().split())) for _ in range(n-1)]
uvw.sort(key=lambda x:x[2])
rank = [-1 for _ in range(n)]
ans = 0
for (u, v, w) in uvw:
    u, v = u-1, v-1
    size_u = size(u)
    size_v = size(v)
    ans += w * size_u * size_v
    unite(u, v)
    print(u, v, w, size_u, size_v, ans, rank)
print(ans)
