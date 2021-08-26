from sys import setrecursionlimit
setrecursionlimit(10**7)

n = int(input())
a = list(map(int, input().split()))

g = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(lambda x: int(x)-1, input().split())
    g[u].append(v)
    g[v].append(u)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def dfs(pair, root, res):
    global ans
    for chi in g[pair]:
        if chi == root:
            continue
        tmp = gcd(res, a[chi])
        if tmp == 1:
            ans += 1
        dfs(chi, pair, tmp)


ans = 0
for i in range(n):
    dfs(i, -1, a[i])

print(ans//2)
