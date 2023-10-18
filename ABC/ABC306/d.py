# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
x = []
y = []

for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

dp = [[-INF]*(2) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    if x[i]:
        # 食べる
        dp[i+1][1] = max(dp[i+1][1], dp[i][0]+y[i])

        # 食べない
        dp[i+1][0] = max(dp[i+1][0], dp[i][0])
        dp[i+1][1] = max(dp[i+1][1], dp[i][1])
    else:
        # 食べる
        dp[i+1][0] = max(dp[i+1][0], dp[i][0]+y[i])
        dp[i+1][0] = max(dp[i+1][0], dp[i][1]+y[i])

        # 食べない
        dp[i+1][0] = max(dp[i+1][0], dp[i][0])
        dp[i+1][1] = max(dp[i+1][1], dp[i][1])

print(max(dp[n]))
