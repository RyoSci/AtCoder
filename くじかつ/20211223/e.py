import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

h, w, k = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))

mod = 998244353
dp = [[0]*4 for _ in range(k+1)]

if x1 == x2 and y1 == y2:
    dp[0] = [1, 1, 1, 0]
elif x1 == x2:
    dp[0] = [0, 1, 0, 0]
elif y1 == y2:
    dp[0] = [1, 0, 0, 0]
elif x1 != x2 and y1 != y2:
    dp[0] = [0, 0, 0, 1]

for i in range(k):
    dp[i + 1][0] = ((dp[i][0] * (h - 1)) %
                    mod + dp[i][1] - dp[i][2] + dp[i][3]) % mod
    dp[i + 1][1] = ((dp[i][1] * (w - 1)) %
                    mod + dp[i][0] - dp[i][2] + dp[i][3]) % mod
    dp[i + 1][2] = (dp[i][0] + dp[i][1] - 2 * dp[i][2]) % mod
    dp[i + 1][3] = ((dp[i][0] - dp[i][2]) * (w - 1) % mod +
                    (dp[i][1] - dp[i][2]) * (h - 1) % mod +
                    dp[i][3] * (h - 2 + w - 2) % mod) % mod
    for j in range(4):
        dp[i + 1][j] %= mod

print(dp[-1][2])
