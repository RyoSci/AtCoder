# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
x = list(map(int, input().split()))
c = [0]*(n+1)
for i in range(m):
    ci, yi = map(int, input().split())
    c[ci] = yi

dp = [[-INF]*(n+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == -INF:
            continue
        # 表が出た
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+x[i]+c[j+1])
        # 裏が出た
        dp[i+1][0] = max(dp[i+1][0], dp[i][j])

ans = -INF
for i in range(n+1):
    ans = max(ans, dp[n][i])

print(ans)
