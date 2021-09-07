import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]

m = sum(s)
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        if j+s[i] <= m:
            dp[i+1][j+s[i]] = max(dp[i+1][j+s[i]], dp[i][j]+s[i])

res = 0
for i in range(m+1):
    if dp[-1][i] % 10 == 0:
        continue
    res = max(res, dp[-1][i])

print(res)
