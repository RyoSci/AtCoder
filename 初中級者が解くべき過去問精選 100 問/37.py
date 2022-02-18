n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = [[10**6]*(n+1) for i in range(m+1)]
dp[0][0] = 0

for i in range(m):
    ci = c[i]
    for j in range(n+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if 0 <= j+ci < n+1:
            dp[i+1][j+ci] = min(dp[i+1][j+ci], dp[i][j]+1)
        if 0 <= j+ci < n+1:
            dp[i+1][j+ci] = min(dp[i+1][j+ci], dp[i+1][j]+1)

print(dp[-1][-1])
