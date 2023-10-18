# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**9

n, d = map(int, input().split())
a = []
for _ in range(d):
    ai = list(map(int, input().split()))
    a.append(ai)

dp = [[INF]*(3) for _ in range(n)]
for i in range(n):
    dp[i][0] = a[0][i]

for i in range(1, d):
    ndp = [[INF]*(3) for _ in range(n)]

    tot = []

    for j in range(n):
        tmp = INF
        for k in range(3):
            tmp = min(tmp, dp[j][k])
        tot.append((tmp, j))

    tot.sort()

    for j in range(n):
        # １連
        if j != tot[0][1]:
            ndp[j][0] = min(ndp[j][0], tot[0][0]+a[i][j])
        else:
            ndp[j][0] = min(ndp[j][0], tot[1][0]+a[i][j])

        # ２連
        ndp[j][1] = min(ndp[j][1], dp[j][0]+a[i][j]//10*9)
        # ３連
        ndp[j][2] = min(ndp[j][2], dp[j][1]+a[i][j]//10*7)
        ndp[j][2] = min(ndp[j][2], dp[j][2]+a[i][j]//10*7)

    dp = ndp

ans = INF
for i in range(n):
    for j in range(3):
        ans = min(ans, dp[i][j])

print(ans)
