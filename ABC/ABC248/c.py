# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, k = list(map(int, input().split()))

dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
MOD = 998244353
for i in range(n):
    for j in range(k+1):
        if dp[i][j] == 0:
            continue
        for kk in range(1, m+1):
            if j+kk <= k:
                dp[i+1][j+kk] += dp[i][j]
                dp[i+1][j+kk] %= MOD

ans = 0
for i in range(1, k+1):
    ans += dp[n][i]
    ans %= MOD

print(ans)
