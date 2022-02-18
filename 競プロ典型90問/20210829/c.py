import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)
    g[b].append(a)


def dfs(pair, root=-1):
    for chi in g[pair]:
        if chi == root:
            continue
        dis[chi] = dis[pair]+1
        dfs(chi, pair)


dis = [0]*n
dfs(0)

max_dis = 0
max_index = -1
for i in range(n):
    if max_dis < dis[i]:
        max_dis = dis[i]
        max_index = i

dis = [0]*n
dfs(max_index)

print(max(dis)+1)
