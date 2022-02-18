from abc import abstractproperty
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append([b, c])
    g[b].append([a, c])

q, k = map(int, input().split())
dis = [0]*n


def dfs(pair, root=-1):
    for chi, c in g[pair]:
        if chi == root:
            continue
        dis[chi] = dis[pair]+c
        dfs(chi, pair)


dfs(k-1)

for i in range(q):
    x, y = map(lambda x: int(x)-1, input().split())
    print(dis[x]+dis[y])
