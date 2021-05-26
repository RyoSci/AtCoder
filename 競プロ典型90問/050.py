n, l = map(int, input().split())
dp = [0]*(n+1)
dp[0] = 1
mod = 10**9+7

for i in range(n):
    dp[i+1] = (dp[i+1] + dp[i]) % mod
    if i+l <= n:
        dp[i+l] = (dp[i+l]+dp[i]) % mod

print(dp[-1])
