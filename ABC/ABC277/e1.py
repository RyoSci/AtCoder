# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from heapq import *
from collections import deque
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, k = map(int, input().split())
gz = [[] for _ in range(n)]
go = [[] for _ in range(n)]
for i in range(m):
    u, v, a = map(int, input().split())
    u -= 1
    v -= 1
    if a == 0:
        gz[u].append(v)
        gz[v].append(u)
    else:
        go[u].append(v)
        go[v].append(u)

tmp = list(map(int, input().split()))
s = [0]*n
for i in tmp:
    s[i-1] = 1

dis_z = [INF]*n
dis_o = [INF]*n

dis_o[0] = 0


q = []
heapify(q)
heappush(q, (0, 0))

sw = deque()
if s[0] == 1:
    sw.append(0)


now = 1

while len(q) > 0:
    d, x = heappop(q)
    if now:
        if d > dis_o[x]:
            continue
        for nx in go[x]:
            if s[nx] == 1:
                sw.append(nx)
            if dis_o[nx] > dis_o[x]+1:
                dis_o[nx] = dis_o[x]+1
                heappush(q, (dis_o[nx], nx))
    else:
        if d > dis_z[x]:
            continue
        for nx in gz[x]:
            if s[nx] == 1:
                sw.append(nx)
            if dis_z[nx] > dis_z[x]+1:
                dis_z[nx] = dis_z[x]+1
                heappush(q, (dis_z[nx], nx))

    if len(q) == 0 and len(sw) > 0:
        while len(sw) > 0:
            nx = sw.popleft()
            if now and dis_z[nx] > dis_o[nx]:
                dis_z[nx] = dis_o[nx]
                heappush(q, (dis_z[nx], nx))
            if now == 0 and dis_o[nx] > dis_z[nx]:
                dis_o[nx] = dis_z[nx]
                heappush(q, (dis_o[nx], nx))

        now ^= 1

ans = min(dis_o[n-1], dis_z[n-1])
if ans == INF:
    print(-1)
else:
    print(ans)
