a, b, c = map(int, input().split())

dp = [[[[0, 0] for k in range(101)] for j in range(101)] for i in range(101)]
dp[a][b][c] = [0, 1]

for i in range(a, 100):
    for j in range(b, 100):
        for k in range(c, 100):
            cnt, now = dp[i][j][k]
            if 1 < i+1 < 101:
                dp[i+1][j][k][0] = cnt+1
                dp[i+1][j][k][1] += now*i/(i+j+k)
            if 1 < j+1 < 101:
                dp[i][j+1][k][0] = cnt+1
                dp[i][j+1][k][1] += now*j/(i+j+k)
            if 1 < k+1 < 101:
                dp[i][j][k+1][0] = cnt+1
                dp[i][j][k+1][1] += now*k/(i+j+k)

res = 0
for i in range(100):
    for j in range(100):
        cnt, now = dp[100][i][j]
        res += cnt*now
        cnt, now = dp[i][100][j]
        res += cnt*now
        cnt, now = dp[i][j][100]
        res += cnt*now

print(res)
