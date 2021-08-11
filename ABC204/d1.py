n = int(input())
t = list(map(int, input().split()))
sum_t = sum(t)
dp = [[0]*(sum_t+1) for _ in range(n+1)]

for i in range(n):
    for j in range(sum_t+1):
        if j+t[i] <= sum_t:
            dp[i+1][j+t[i]] = max(dp[i+1][j+t[i]], dp[i][j]+t[i])
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

res = 10**6
for i in range(sum_t+1):
    tmp = max(sum_t-dp[-1][i], dp[-1][i])
    res = min(res, tmp)

print(res)
