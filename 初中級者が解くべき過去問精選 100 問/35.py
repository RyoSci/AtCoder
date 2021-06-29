n, w = map(int, input().split())
vw = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(w+1) for _ in range(n+1)]

for i in range(n):
    vi, wi = vw[i]
    for j in range(w+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if 0 <= j+wi <= w:
            dp[i+1][j+wi] = max(dp[i+1][j+wi], dp[i][j]+vi)

print(dp[-1][-1])
