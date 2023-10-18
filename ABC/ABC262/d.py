# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
MOD = 998244353
n = int(input())
a = list(map(int, input().split()))

ans = n
for x in range(2, n+1):
    dp = [[[0]*x for i in range(x+1)] for j in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(x+1):
            for k in range(x):
                if dp[i][j][k] == 0:
                    continue
                # 使う
                if j+1 <= x:
                    dp[i+1][j+1][(k+a[i]) % x] += dp[i][j][k]
                    dp[i+1][j+1][(k+a[i]) % x] %= MOD
                # 使わない
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= MOD
    ans += dp[n][x][0]
    ans %= MOD
# print(dp)
print(ans)
