# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, q = map(int, input().split())
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    l, r = map(int, input().split())
    dp[l][r] += 1

for l in range(1, n):
    for r in range(n, l, -1):
        # dp[l][r] += dp[l][l]+dp[r][r]
        for m in range(l, r+1):
            dp[l][r] += dp[l][m]+dp[m][r]

for i in range(q):
    p, q = map(int, input().split())
    print(dp[p][q])


# for i in range(n+1):
#     print(dp[i])
