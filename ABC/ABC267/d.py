# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-INF]*(m+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(m+1):
        if dp[i][j] == -INF:
            continue
        # 使わない
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        # 使う
        if j+1 <= m:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+a[i]*(j+1))

print(dp[n][m])
