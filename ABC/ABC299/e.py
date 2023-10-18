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
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)


can = [1] * n


def bfs1(pi, di):
    dis = [INF]*n
    dis[pi] = 0
    q = deque()
    q.append(pi)
    while len(q):
        par = q.popleft()
        if dis[par] < di:
            can[par] = 0
        for chi in g[par]:
            if dis[chi] == INF and dis[par]+1 <= di:
                dis[chi] = dis[par]+1
                q.append(chi)


k = int(input())
p = []
d = []
for i in range(k):
    pi, di = map(int, input().split())
    pi -= 1
    p.append(pi)
    d.append(di)

    bfs1(pi, di)


def bfs2(pi):
    dis = [INF]*n
    dis[pi] = 0
    q = deque()
    q.append(pi)
    while len(q):
        par = q.popleft()
        if can[par] == 1:
            mindis[pi] = dis[par]
            break

        for chi in g[par]:
            if dis[chi] == INF:
                dis[chi] = dis[par] + 1
                q.append(chi)


mindis = [-1]*n

for i in range(n):
    bfs2(i)


for i in range(k):
    if mindis[p[i]] != d[i]:
        print("No")
        exit()
else:
    print("Yes")
    print(*can, sep="")
