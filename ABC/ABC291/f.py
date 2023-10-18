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
rg = [[] for _ in range(n)]


s = [""]*n
for i in range(n):
    s[i] = input()
    for j in range(m):
        if s[i][j] == "1":
            g[i].append(i+j+1)
            rg[i+j+1].append(i)


dis = [INF]*n
dis[0] = 0
q = deque()
q.append(0)
while len(q):
    par = q.popleft()
    for chi in g[par]:
        if dis[chi] == INF:
            dis[chi] = dis[par]+1
            q.append(chi)

rdis = [INF]*n
rdis[n-1] = 0
q = deque()
q.append(n-1)
while len(q):
    par = q.popleft()
    for chi in rg[par]:
        if rdis[chi] == INF:
            rdis[chi] = rdis[par]+1
            q.append(chi)

ans = []
for k in range(1, n-1):
    d = INF
    for i in range(1, m):
        prek = k-i
        if prek < 0:
            break
        for j in range(m):
            nexk = prek+j+1
            if nexk <= k or n <= k:
                continue
            if s[prek][j] == "1":
                d = min(d, dis[prek]+1+rdis[nexk])
    if d == INF:
        d = -1
    ans.append(d)

print(*ans)
