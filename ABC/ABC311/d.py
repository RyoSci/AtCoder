# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
s = []

for i in range(n):
    si = input()
    s.append(list(si))


q = deque()
dp = [[[0]*(4) for j in range(m)] for i in range(n)]
for i in range(4):
    dp[1][1][i] = 1
    q.append((1, 1, i))

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


while len(q):
    i, j, d = q.popleft()

    ni = i+di[d]
    nj = j+dj[d]

    if not (0 <= ni < n and 0 <= nj < m):
        continue
    if dp[ni][nj][d]:
        continue
    dp[ni][nj][d] = 1
    if s[ni][nj] == "#":
        for k in range(4):
            q.append((i, j, k))
    else:
        q.append((ni, nj, d))

ans = 0
for i in range(n):
    for j in range(m):
        if s[i][j] == "#":
            continue
        cnt = 0
        for k in range(4):
            cnt += dp[i][j][k]

        if cnt > 0:
            ans += 1
print(ans)
