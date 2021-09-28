import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
g = []
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g.append([c, a, b])

g.sort()


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
    p[py] = px
    return


p = [-1]*n

res = 0
for i in range(m):
    c, a, b = g[i]
    if find(a) == find(b):
        if c > 0:
            res += c
        continue
    else:
        union(a, b)

print(res)
