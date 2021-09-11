import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def find(x):
    if p[x] < 0:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        return
    p[px] += p[py]
    p[py] = x
    return


v, e = map(int, input().split())


p = [-1]*v

edge = []
for i in range(e):
    s, t, w = map(int, input().split())
    edge.append([w, s, t])

edge.sort()

res = 0
for i in range(e):
    w, u, v = edge[i]
    if find(u) == find(v):
        continue
    union(u, v)
    res += w

print(res)
