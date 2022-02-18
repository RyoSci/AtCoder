import heapq
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m = map(int, input().split())
h = list(map(int, input().split()))

g = [[] for _ in range(n)]

for i in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    if h[u] > h[v]:
        g[u].append((v, -(h[u]-h[v])))
        g[v].append((u, 2*(h[u]-h[v])))
    elif h[u] < h[v]:
        g[u].append((v, 2*(h[v]-h[u])))
        g[v].append((u, -(h[v]-h[u])))
    else:
        g[u].append((v, 0))
        g[v].append((u, 0))

INF = 10**18
dis = [-INF]*n
dis[0] = 0

q = []
heapq.heapify(q)
# (0からのdis, 頂点番号)
heapq.heappush(q, [0, 0])
ans = 0
while len(q) > 0:
    d, v = heapq.heappop(q)
    d = -d
    if dis[v] > d:
        continue
    for nv, c in g[v]:
        c = -c
        if dis[nv] < dis[v]+c:
            dis[nv] = dis[v]+c
            ans = max(ans, dis[nv])
            heapq.heappush(q, [-dis[nv], nv])

print(ans)
