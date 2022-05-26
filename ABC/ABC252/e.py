# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from heapq import heapify, heappop, heappush
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    g[a].append([b, c, i])
    g[b].append([a, c, i])


q = []
heappush(q, [0, 0, -1])

dis = [INF]*n
dis[0] = 0

ans = []
while len(q) > 0:
    d, par, i = heappop(q)
    if dis[par] < d:
        continue
    ans.append(i+1)
    for chi, dd, i in g[par]:
        if dis[chi] > dis[par]+dd:
            dis[chi] = dis[par]+dd
            heappush(q, [dis[chi], chi, i])

print(*ans[1:])
