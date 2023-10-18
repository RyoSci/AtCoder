# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

x, y, z = map(int, input().split())
s = input()
n = len(s)

dp = [[INF]*2 for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    if s[i] == "a":
        # ON
        dp[i+1][1] = min(dp[i+1][1], dp[i][1]+y)
        dp[i+1][0] = min(dp[i+1][0], dp[i][1]+z+x)

        # OFF
        dp[i+1][1] = min(dp[i+1][1], dp[i][0]+z+y)
        dp[i+1][0] = min(dp[i+1][0], dp[i][0]+x)
    else:
        # ON
        dp[i+1][1] = min(dp[i+1][1], dp[i][1]+x)
        dp[i+1][0] = min(dp[i+1][0], dp[i][1]+z+y)

        # OFF
        dp[i+1][1] = min(dp[i+1][1], dp[i][0]+z+x)
        dp[i+1][0] = min(dp[i+1][0], dp[i][0]+y)

print(min(dp[n]))
