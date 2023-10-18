# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
mod = 998244353
l = n
r = 3
dp = [[0]*2 for _ in range(n)]
dp[0][0] = m*(m-1)
dp[0][0] %= mod
i = 0
while 1:
    if (l - 1) % n == r % n:
        dp[i+1][0] = dp[i][1]*((m-1)**2-(m-1)) + dp[i][0]*((m-1)**2-(m-2))
        break

    elif l % n == r % n:
        dp[i+1][0] = dp[i][1]*(m-1) + dp[i][0]*(m-2)
        dp[i+1][0] %= mod
        break

    else:
        dp[i+1][0] = dp[i][1]*((m-1)**2-(m-1)) + dp[i][0]*((m-1)**2-(m-2))
        dp[i+1][0] %= mod

        dp[i+1][1] = dp[i][1]*(m-1) + dp[i][0]*(m-2)
        dp[i+1][1] %= mod

    i += 1
    l -= 1
    l %= n
    r += 1
    r %= n

if n > 2:
    print(dp[i+1][0] % mod)
else:
    print(dp[0][0] % mod)
