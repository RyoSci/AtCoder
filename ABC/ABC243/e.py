# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())


INF = 10**18
dp = [[INF]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

edges = []

for i in range(m):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    dp[a][b] = c
    dp[b][a] = c

    edges.append([a, b, c])


for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[i][k] != INF and dp[k][j] != INF:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = 0
for i in range(m):
    a, b, c = edges[i]
    if dp[a][b] < c:
        ans += 1
    elif dp[a][b] == c:
        cnt = 0
        for k in range(n):
            if dp[a][b] == dp[a][k]+dp[k][b]:
                cnt += 1
        if cnt > 2:
            ans += 1


print(ans)
