# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, k = map(int, input().split())

dp = [[0]*(n+1) for _ in range(k+1)]
dp[0][0] = 1
MOD = 998244353
for i in range(k):
    for j in range(n):
        for l in range(1, m+1):
            if j+l <= n:
                dp[i+1][j+l] += dp[i][j]
                dp[i+1][j+l] %= MOD
            else:
                dp[i+1][n-(j+l-n)] += dp[i][j]
                dp[i+1][n-(j+l-n)] %= MOD

ans = 0
inv = [0]*(k+1)
inv[k] = pow(pow(m, k, MOD), MOD-2, MOD)
for i in range(k-1, -1, -1):
    inv[i] = inv[i+1]*m
    inv[i] %= MOD

for i in range(1, k+1):
    ans += dp[i][n]*inv[i]
    ans %= MOD

print(ans)
