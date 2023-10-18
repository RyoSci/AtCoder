from sys import stdin
from collections import deque


def rerooting():
    dp = [[E]*len(edge[v]) for v in range(n)]

    # dfs1
    memo = [E]*n
    for v in order[::-1]:
        res = E
        for i in range(len(edge[v])):
            if edge[v][i] == par[v]:
                continue
            dp[v][i] = memo[edge[v][i]]
            res = merge(res, f(dp[v][i], edge[v][i]))
        memo[v] = g(res, v)

    # dfs2
    memo2 = [E]*n
    for v in order:
        for i in range(len(edge[v])):
            if edge[v][i] == par[v]:
                dp[v][i] = memo2[v]

        s = len(edge[v])
        cumR = [E]*(s+1)
        cumR[s] = E
        for i in range(s, 0, -1):
            cumR[i-1] = merge(cumR[i], f(dp[v][i-1], v))

        cumL = E
        for i in range(s):
            if edge[v][i] != par[v]:
                val = val = merge(cumL, cumR[i+1])
                memo2[edge[v][i]] = g(val, v)
            cumL = merge(cumL, f(dp[v][i], edge[v][i]))

    ans = [E for i in range(n)]

    for v in range(n):
        res = E
        for i in range(len(edge[v])):
            res = merge(res, f(dp[v][i], edge[v][i]))
        ans[v] = g(res, v)

    return ans


E = (1, 0)


def f(res, v):
    x, y = res
    return (x*finv[y] % mod, y)


def g(res, v):
    x, y = res
    return (x*fac[y] % mod, y+1)


def merge(a, b):
    ax, ay = a
    bx, by = b
    return (ax*bx % mod, ay+by)


def input(): return stdin.readline()[:-1]


mod = 10**9+7

m = 2*10**5+10
fac = [1]*m
for i in range(1, m):
    fac[i] = fac[i-1]*i % mod
finv = [1]*m
finv[-1] = pow(fac[-1], mod-2, mod)
for i in range(m-2, -1, -1):
    finv[i] = finv[i+1]*(i+1) % mod

n = int(input())
edge = [[] for i in range(n)]
for i in range(n-1):
    x, y = map(lambda x: int(x)-1, input().split())
    edge[x].append(y)
    edge[y].append(x)


order = []
par = [-1]*n
todo = deque([0])
while todo:
    v = todo.popleft()
    order.append(v)
    for u in edge[v]:
        if u != par[v]:
            par[u] = v
            todo.append(u)

ans = rerooting()
for i in ans:
    print(i[0])
