from collections import deque
from sys import setrecursionlimit
setrecursionlimit(10**6)

n, m = map(int, input().split())
a = list(map(int, input().split()))

g = [[] for _ in range(n)]
for i in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    g[x].append(y)


def dfs(pair, cnt):
    global res
    p[pair] = 1
    for chi in g[pair]:
        res = max(res, a[chi]-cnt)
        dfs(chi, min(cnt, a[chi]))


def bfs(pair, cnt):
    global res
    q = deque()
    q.append([pair, cnt])
    while len(q) != 0:
        pair, cnt = q.popleft()
        p[pair] = 1
        for chi in g[pair]:
            res = max(res, a[chi]-cnt)
            q.append([chi, min(cnt, a[chi])])


p = [0]*n
res = -10**18
for i in range(n):
    if p[i] == 0:
        bfs(i, a[i])

print(res)
