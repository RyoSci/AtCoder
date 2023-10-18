# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x, y = list(map(int, input().split()))

dp = [[0]*2 for _ in range(n+1)]
dp[n][1] = 1

for i in range(n, 1, -1):
    dp[i-1][1] += dp[i][1]
    dp[i][0] += dp[i][1]*x

    dp[i-1][1] += dp[i][0]
    dp[i-1][0] += dp[i][0]*y

print(dp[1][0])
