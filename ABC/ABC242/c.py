# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
dp = [[0]*9 for _ in range(n)]
for i in range(9):
    dp[0][i] = 1

mod = 998244353
for i in range(n-1):
    for j in range(9):
        if j > 0:
            dp[i+1][j] += dp[i][j-1]
        dp[i+1][j] %= mod
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod
        if j < 8:
            dp[i+1][j] += dp[i][j+1]
        dp[i+1][j] %= mod

ans = 0
for i in range(9):
    ans += dp[n-1][i]
    ans %= mod

print(ans)
