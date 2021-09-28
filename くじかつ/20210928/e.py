import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = [[]*n for _ in range(n)]
edge = dict()
for i in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    edge[(u, v)] = w
    edge[(v, u)] = w


def dfs(pair, root=-1):
    for chi in g[pair]:
        if chi == root:
            continue
        dis[chi] = dis[pair]+edge[(pair, chi)]
        dis[chi] %= 2
        dfs(chi, pair)


dis = [0]*n

dfs(0)

print(*dis, sep="\n")
