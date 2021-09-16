n, w = map(int, input().split())
dp = [[0]*(w+10) for _ in range(n+10)]

for i in range(n):
    wi, vi = map(int, input().split())
    for j in range(w+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j+wi < w+1:
            dp[i+1][j+wi] = max(dp[i+1][j+wi], dp[i][j]+vi)

print(dp[n][w])
