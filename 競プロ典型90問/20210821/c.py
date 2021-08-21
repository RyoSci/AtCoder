n = int(input())
s = input()

dp = [[0]*(n+1) for _ in range(8)]
for j in range(n+1):
    dp[0][j] = 1

atcoder = "atcoder"
mod = 10**9+7
for i in range(7):
    for j in range(n):
        if atcoder[i] == s[j]:
            dp[i+1][j+1] += dp[i][j]
        dp[i+1][j+1] += dp[i+1][j]
        dp[i+1][j+1] %= mod

print(dp[-1][-1])
