# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()

n = len(s)
dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1

mod = 998244353
for i in range(n):
    for j in range(n+1):

        if s[i] == "(":
            if j < n:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= mod

        elif s[i] == ")":
            if j > 0:
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j-1] %= mod

        else:
            if j < n:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= mod
            if j > 0:
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j-1] %= mod

print(dp[n][0])
