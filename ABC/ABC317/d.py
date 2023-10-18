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
z = []

for i in range(n):
    xi, yi, zi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    z.append(zi)

m = 10**5+10
dp = [[INF]*(m) for _ in range(n+1)]
# dp = [INF]*m

dp[0][0] = 0

for i in range(n):
    xi, yi, zi = x[i], y[i], z[i]

    if xi > yi:
        for j in range(m):
            if j + zi < m:
                dp[i+1][j+zi] = min(dp[i+1][j+zi], dp[i][j])
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    else:
        tmp = abs(yi-xi)//2 + 1
        for j in range(m):
            if j + zi < m:
                dp[i+1][j+zi] = min(dp[i+1][j+zi], dp[i][j]+tmp)
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])

ans = INF
tot = sum(z)//2+1
for i in range(tot, sum(z)+1):
    ans = min(ans, dp[n][i])


# print(dp[:100])
# print(tot)
print(ans)
