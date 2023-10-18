# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
dp = [[INF]*2 for _ in range(n)]

ans = INF

dp[0][1] = a[0]
for i in range(n-1):
    # 使っていない
    dp[i+1][1] = min(dp[i+1][1], dp[i][0]+a[i+1])
    # 使っている
    dp[i+1][1] = min(dp[i+1][1], dp[i][1]+a[i+1])
    dp[i+1][0] = min(dp[i+1][0], dp[i][1])

ans = min(ans, dp[n-1][0], dp[n-1][1])
# print(dp)

dp[0][0] = 0
for i in range(n-1):
    # 使っていない
    dp[i+1][1] = min(dp[i+1][1], dp[i][0]+a[i+1])
    # 使っている
    dp[i+1][1] = min(dp[i+1][1], dp[i][1]+a[i+1])
    dp[i+1][0] = min(dp[i+1][0], dp[i][1])

ans = min(ans, dp[n-1][1])
# print(dp)
print(ans)
