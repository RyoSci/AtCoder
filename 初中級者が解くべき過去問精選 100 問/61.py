n, m = map(int, input().split())

INF = 10**18

dp = [[INF if i != j else 0 for j in range(n)] for i in range(n)]

for i in range(m):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = t
    dp[b][a] = t

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[i][k] == INF or dp[k][j] == INF:
                continue
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])


res = INF
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp = max(tmp, dp[i][j])
    res = min(res, tmp)

print(res)
