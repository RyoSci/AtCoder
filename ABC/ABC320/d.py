# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1

    g[a].append((b, x, y))
    g[b].append((a, -x, -y))

q = deque()

pos = [-1]*n
pos[0] = (0, 0)
q.append(0)

while len(q):
    par = q.popleft()

    for chi, dx, dy in g[par]:
        px, py = pos[par]
        nx = px+dx
        ny = py+dy

        if pos[chi] == -1:
            pos[chi] = (nx, ny)
            q.append(chi)
        elif pos[chi] != -1:
            if pos[chi] != (nx, ny):
                pos[chi] = INF


for i in range(n):
    if pos[i] == -1 or pos[i] == INF:
        print("undecidable")
    else:
        print(*pos[i])
