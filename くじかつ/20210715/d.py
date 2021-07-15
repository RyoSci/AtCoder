n, m = map(int, input().split())

dp = [[10**18]*n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = c

for i in range(n):
    dp[i][i] = 0

res = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
            if dp[i][j] != 10**18:
                res += dp[i][j]
print(res)
