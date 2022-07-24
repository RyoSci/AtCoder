# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, c = map(int, input().split())
t = []
a = []
for i in range(n):
    ti, ai = map(int, input().split())
    t.append(ti)
    a.append(ai)


def _(N, M, K): return (N * (n+1) + M) * 2 + K


dp = [0] * 30 * (n+1) * 2
# dp = [[[0]*2 for j in range(n+1)] for i in range(30)]
for i in range(30):
    # dp[i][0][1] = 1
    dp[_(i, 0, 1)] = 1


# 各bitごと
for i in range(30):
    for j in range(n):
        if t[j] == 1:
            # dp[i][j+1][0] = dp[i][j][0] & (a[j] >> i & 1)
            # dp[i][j+1][1] = dp[i][j][1] & (a[j] >> i & 1)
            dp[_(i, j+1, 0)] = dp[_(i, j, 0)] & (a[j] >> i & 1)
            dp[_(i, j+1, 1)] = dp[_(i, j, 1)] & (a[j] >> i & 1)

        elif t[j] == 2:
            # dp[i][j+1][0] = dp[i][j][0] | (a[j] >> i & 1)
            # dp[i][j+1][1] = dp[i][j][1] | (a[j] >> i & 1)
            dp[_(i, j+1, 0)] = dp[_(i, j, 0)] | (a[j] >> i & 1)
            dp[_(i, j+1, 1)] = dp[_(i, j, 1)] | (a[j] >> i & 1)

        else:
            # dp[i][j+1][0] = dp[i][j][0] ^ (a[j] >> i & 1)
            # dp[i][j+1][1] = dp[i][j][1] ^ (a[j] >> i & 1)
            dp[_(i, j+1, 0)] = dp[_(i, j, 0)] ^ (a[j] >> i & 1)
            dp[_(i, j+1, 1)] = dp[_(i, j, 1)] ^ (a[j] >> i & 1)

ans = c
for i in range(n):
    tmp = 0
    for j in range(30):
        # tmp += dp[j][i+1][ans >> j & 1] << j
        tmp += dp[_(j, i+1, ans >> j & 1)] << j
    ans = tmp
    print(ans)
