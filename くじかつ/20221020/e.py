# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from heapq import *
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, c, i))
    g[b].append((a, c, i))

dis = [INF]*n
dis[0] = 0


q = []
heapify(q)
q.append((dis[0], 0, -1))

ans = []
while len(q) > 0:
    d, par, i = heappop(q)
    if dis[par] < d:
        continue
    ans.append(i+1)
    for chi, c, j in g[par]:
        if dis[chi] > dis[par]+c:
            dis[chi] = dis[par]+c
            heappush(q, (dis[chi], chi, j))

print(*ans[1:])

