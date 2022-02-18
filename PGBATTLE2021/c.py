import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, a, b = list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][0] = 1
mod = 998244353

for i in range(n+1):
    for j in range(m+1):
        if i+1 == a and j == b:
            pass
        else:
            if i+1 <= n and j <= m:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= mod

        if i == a and j+1 == b:
            pass
        else:
            if i <= n and j+1 <= m:
                dp[i][j+1] += dp[i][j]
                dp[i][j+1] %= mod

print(dp[n][m] % mod)
