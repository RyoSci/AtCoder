# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
MOD = 998244353
n, m, k = list(map(int, input().split()))
g = [[i] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

dp = [[0]*n for _ in range(k+1)]
dp[0][0] = 1
for i in range(k):
    tot = 0
    for j in dp[i]:
        tot += j
        tot %= MOD

    for par in range(n):
        now = tot
        for chi in g[par]:
            now -= dp[i][chi]
            now %= MOD
        dp[i+1][par] = now

print(dp[k][0])
