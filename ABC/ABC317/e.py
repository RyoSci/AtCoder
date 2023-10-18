# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
from bisect import bisect_left
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
a = []
cols = [[] for _ in range(h)]
rows = [[] for _ in range(w)]
for i in range(h):
    ai = list(input())
    a.append(ai)

    for j in range(w):
        if ai[j] != "." and ai[j] != "S" and ai[j] != "G":
            cols[i].append(j)
            rows[j].append(i)
        if ai[j] == "S":
            s = (i, j)
        if ai[j] == "G":
            g = (i, j)


ok = [[0]*(w) for _ in range(h)]


for i in range(h):
    for j in range(w):
        if a[i][j] != "." and a[i][j] != "S" and a[i][j] != "G":
            continue

        flag = True
        pos = bisect_left(cols[i], j)
        if pos != 0:
            left = pos-1
            nj = cols[i][left]

            if a[i][nj] == ">":
                flag = False

        if pos != len(cols[i]):
            right = pos
            nj = cols[i][right]

            if a[i][nj] == "<":
                flag = False

        pos = bisect_left(rows[j], i)
        if pos != 0:
            left = pos-1
            ni = rows[j][left]

            if a[ni][j] == "v":
                flag = False

        if pos != len(rows[j]):
            right = pos
            ni = rows[j][right]

            if a[ni][j] == "^":
                flag = False

        if flag:
            ok[i][j] = 1


q = deque()
q.append(s)
dis = [[INF]*(w) for _ in range(h)]
dis[s[0]][s[1]] = 0

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


while len(q):
    now = q.popleft()
    (i, j) = now

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < h and 0 <= nj < w and a[ni][nj] not in {"#", ">", "v", "^"}:
            if ok[ni][nj] and dis[ni][nj] > dis[i][j]+1:
                dis[ni][nj] = dis[i][j]+1

                q.append((ni, nj))


if dis[g[0]][g[1]] == INF:
    print(-1)
else:
    print(dis[g[0]][g[1]])
