# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
p = list(map(int, input().split()))

g = [[] for _ in range(n)]
for i in range(n-1):
    g[p[i]-1].append(i+1)

dp = [-1]*n
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    dp[x] = max(dp[x], y)


def dfs(par):
    for chi in g[par]:
        dp[chi] = max(dp[chi], dp[par]-1)
        dfs(chi)


dfs(0)
ans = 0
for i in range(n):
    if dp[i] >= 0:
        ans += 1

print(ans)
