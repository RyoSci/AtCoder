# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0]*2 for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(n-1):
    if dp[i][0] != 0:
        if abs(a[i+1]-a[i]) <= k:
            dp[i+1][0] = dp[i][0]
        if abs(b[i+1]-a[i]) <= k:
            dp[i+1][1] = dp[i][0]
    if dp[i][1] != 0:
        if abs(a[i+1]-b[i]) <= k:
            dp[i+1][0] = dp[i][1]
        if abs(b[i+1]-b[i]) <= k:
            dp[i+1][1] = dp[i][1]


if dp[n-1][0] == 1 or dp[n-1][1] == 1:
    print("Yes")
else:
    print("No")
