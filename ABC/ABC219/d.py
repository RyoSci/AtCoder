import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
inf = 10**18
dp = [[[inf for k in range(y+1)] for j in range(x+1)] for i in range(n+1)]
dp[0][0][0] = 0

a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

for i in range(n):
    ai, bi = a[i], b[i]
    for j in range(x+1):
        for k in range(y+1):
            nj = min(j+ai, x)
            nk = min(k+bi, y)
            dp[i+1][nj][nk] = min(dp[i+1][nj][nk], dp[i][j][k]+1)
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])

if dp[n][x][y] != inf:
    print(dp[n][x][y])
else:
    print(-1)
