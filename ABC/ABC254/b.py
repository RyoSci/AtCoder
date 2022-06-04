# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
dp = [[] for _ in range(n)]
dp[0].append(1)
for i in range(1, n):
    dp[i].append(1)
    for j in range(1, i):
        dp[i].append(dp[i-1][j-1]+dp[i-1][j])
    dp[i].append(1)

for i in range(n):
    print(*dp[i])
