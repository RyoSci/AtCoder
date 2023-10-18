# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())

p = [0]*n
g = [[] for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    p[x] += 1
    g[y].append(x)


q = deque()

for i in range(n):
    if p[i] == 0:
        q.append(i)

ans = [-1]*n
cnt = n
while len(q):
    if len(q) > 1:
        break

    par = q.popleft()
    ans[par] = cnt
    cnt -= 1
    for chi in g[par]:
        p[chi] -= 1
        if p[chi] == 0:
            q.append(chi)


if -1 in ans:
    print("No")
else:
    print("Yes")
    print(*ans)
