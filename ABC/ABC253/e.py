# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

MOD = 998244353
n, m, k = list(map(int, input().split()))

dp = [[0]*(m+1) for i in range(n)]
for i in range(1, m+1):
    dp[0][i] = 1

for i in range(1, n):
    pre = dp[i-1][:]
    tot = 0

    for j in range(1, m+1):
        tot += pre[j]
        tot %= MOD
        pre[j] += pre[j-1]
        pre[j] %= MOD

    for j in range(1, m+1):
        if k == 0:
            dp[i][j] += tot
            dp[i][j] %= MOD
        else:
            a = pre[min(m, j+k-1)]
            b = pre[max(0, j-(k-1)-1)]
            now = a-b
            dp[i][j] += tot-now
            dp[i][j] %= MOD

ans = 0
for i in range(1, m+1):
    ans += dp[n-1][i]
    ans %= MOD
print(ans)
