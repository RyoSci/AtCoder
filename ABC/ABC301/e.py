# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w, t = map(int, input().split())
a = []
pos = []
sog = {"SoG"}
for i in range(h):
    ai = list(input())

    a.append(ai)

    for j, aij in enumerate(ai):
        if aij == "S":
            spos = (i, j)
        elif aij == "G":
            gpos = (i, j)
        elif aij == "o":
            pos.append((i, j))

pos = [spos] + pos + [gpos]
# print(pos)

n = len(pos)
dis = [[INF]*(n) for _ in range(n)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(par):
    q = deque()
    q.append(pos[par])
    grid = [[INF]*(w) for _ in range(h)]
    grid[pos[par][0]][pos[par][1]] = 0

    while len(q):
        i, j = q.popleft()
        for di, dj in zip(dx, dy):
            ni = i + di
            nj = j + dj

            if 0 <= ni < h and 0 <= nj < w:
                if a[ni][nj] == "#":
                    continue
                if grid[ni][nj] > grid[i][j]+1:
                    grid[ni][nj] = grid[i][j]+1
                    q.append((ni, nj))

    for i in range(n):
        dis[par][i] = grid[pos[i][0]][pos[i][1]]


for i in range(n):
    bfs(i)

# for i in range(n):
#     print(*dis[i])


m = 1 << (n-2)
dp = [[INF]*(n-2) for _ in range(m)]
for i in range(n-2):
    dp[1 << i][i] = dis[0][i+1]


for i in range(m):
    for j in range(n-2):
        if dp[i][j] == INF:
            continue
        if ((i >> j) & 1) == 0:
            continue
        for k in range(n-2):
            dp[i | 1 << k][k] = min(dp[i | 1 << k][k], dp[i][j]+dis[j+1][k+1])

if dis[0][n-1] > t:
    ans = -1
else:
    ans = 0

for i in range(m):
    cnt = 0
    for j in range(n-2):
        if i >> j & 1:
            cnt += 1

    for j in range(n-2):
        if dp[i][j] + dis[j+1][n-1] <= t:
            ans = max(ans, cnt)

print(ans)
