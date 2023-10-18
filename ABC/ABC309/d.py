# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n1, n2, m = map(int, input().split())

g = [[] for _ in range(n1+n2)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


def bfs(x):
    dis = [INF]*(n1+n2)
    q = deque()
    dis[x] = 0
    q.append(x)

    res = 0
    while len(q):
        par = q.popleft()

        for chi in g[par]:
            if dis[chi] == INF:
                dis[chi] = dis[par]+1
                q.append(chi)
                res = max(res, dis[chi])

    return res


a = bfs(0)
b = bfs(n1+n2-1)

print(a+b+1)
