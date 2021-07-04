import sys
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)
    g[b].append(a)

p = [-1]*n


def dfs(pair, root):
    for chi in g[pair]:
        if p[chi] == -1:
            p[chi] = root
            dfs(chi, root)
    return


for i in range(n):
    if p[i] != -1:
        continue
    p[i] = i
    dfs(i, i)

print(len(set(p))-1)
