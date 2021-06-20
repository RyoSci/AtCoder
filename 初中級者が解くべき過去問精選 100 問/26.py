import sys
sys.setrecursionlimit(10**6)

n, q = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)
    g[b].append(a)

ps = [0]*n
for j in range(q):
    p, x = map(int, input().split())
    p -= 1
    ps[p] += x

passed = [-1]*n


def dfs(pair, cnt):
    passed[pair] = cnt+ps[pair]
    for chi in g[pair]:
        if passed[chi] == -1:
            dfs(chi, passed[pair])


dfs(0, 0)

print(*passed)
