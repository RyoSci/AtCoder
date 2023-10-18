# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = [0]*n
b = [0]*n

for i in range(n):
    a[i], b[i] = map(int, input().split())

dp = [[0]*2 for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 1

mod = 998244353

for i in range(n-1):
    if a[i] != a[i+1]:
        dp[i+1][0] += dp[i][0]
        dp[i+1][0] %= mod
    if a[i] != b[i+1]:
        dp[i+1][1] += dp[i][0]
        dp[i+1][1] %= mod
    if b[i] != a[i+1]:
        dp[i+1][0] += dp[i][1]
        dp[i+1][0] %= mod
    if b[i] != b[i+1]:
        dp[i+1][1] += dp[i][1]
        dp[i+1][1] %= mod

ans = sum(dp[n-1]) % mod
print(ans)
