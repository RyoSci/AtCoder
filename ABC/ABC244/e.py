# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = 10**18

n, m, k, s, t, x = list(map(int, input().split()))
s -= 1
t -= 1
x -= 1
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

dp = [[[0]*2 for i in range(n)] for j in range(k+1)]

dp[0][s][0] = 1
mod = 998244353
for i in range(k):
    for j in range(n):
        for l in range(2):
            if dp[i][j][l] == 0:
                continue
            for chi in g[j]:
                if chi == x:
                    dp[i+1][chi][(l+1) % 2] += dp[i][j][l]
                    dp[i+1][chi][(l+1) % 2] %= mod
                else:
                    dp[i+1][chi][l] += dp[i][j][l]
                    dp[i+1][chi][l] %= mod


print(dp[k][t][0])

# for i in range(k+1):
#     print(dp[i])
