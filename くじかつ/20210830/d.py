import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

h, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

dp = [[10**18]*(h+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    a, b = ab[i]
    for j in range(h+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if j+a <= h:
            dp[i+1][j+a] = min(dp[i+1][j+a], dp[i+1][j]+b)
        else:
            dp[i+1][h] = min(dp[i+1][h], dp[i+1][j]+b)

print(dp[-1][-1])
