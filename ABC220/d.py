import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

mod = 998244353
n = int(input())
a = list(map(int, input().split()))
dp = [[0]*10 for _ in range(n)]
dp[0][a[0]] = 1

for i in range(1, n):
    for j in range(10):
        if dp[i-1][j] > 0:
            dp[i][(j+a[i]) % 10] += dp[i-1][j]
            dp[i][(j+a[i]) % 10] %= mod
            dp[i][(j*a[i]) % 10] += dp[i-1][j]
            dp[i][(j*a[i]) % 10] %= mod

for i in range(10):
    print(dp[n-1][i] % mod)
