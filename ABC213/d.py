from sys import setrecursionlimit
setrecursionlimit(10**7)

n = int(input())
g = [[] for _ in range(n)]

for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(n):
    g[i].sort()

vis = [-1]*n
ans = []


def dfs(pair):
    global ans
    ans.append(pair+1)
    for chi in g[pair]:
        if vis[chi] == -1:
            vis[chi] = 1
            dfs(chi)
            ans.append(pair+1)
    # ans.append(pair+1)
    return


vis[0] = 1
dfs(0)
print(*ans)
