import sys
from types import coroutine
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
# n, m = 10**5, 10**5


INF = 10**18
res = INF
path = []

g = [[]*n for _ in range(n)]
for i in range(m):
    #     a, b = map(lambda x: int(x)-1, input().split())
    a, b = 1, 1+i
    g[a].append(b)

for i in range(n):
    g[i].sort()


visit = [0]*n


def dfs(pair, cnt, s):
    global res, path
    if pair == n-1:
        if res > cnt:
            res = cnt
            path = s[::]
    for chi in g[pair]:
        if visit[chi] == 1:
            continue
        visit[chi] = 1
        s.append(chi+1)
        dfs(chi, cnt+1, s)
    visit[pair] = 0
    s.pop()


visit[0] = 1
dfs(0, 0, [1])

if res == INF:
    print(-1)
else:
    print(*path, sep=" ")
