import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


n, m, k = map(int, input().split())

edge = []
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge.append([c, a, b])

p = [-1]*n


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


edge.sort()

res = []
for i in range(m):
    c, u, v = edge[i]
    if find(u) == find(v):
        continue
    res.append(c)
    union(u, v)

cnt = sum(res)
res.sort(reverse=True)
cnt -= sum(res[:k-1])
print(cnt)
