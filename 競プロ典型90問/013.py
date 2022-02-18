import heapq
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))

INF = 10**18
dis = [INF]*n
dis[0] = 0

q = []
heapq.heapify(q)
# (0からのdis, 頂点番号)
heapq.heappush(q, [0, 0])
while len(q) > 0:
    d, v = heapq.heappop(q)
    if dis[v] < d:
        continue
    for nv, c in g[v]:
        if dis[nv] > dis[v]+c:
            dis[nv] = dis[v]+c
            heapq.heappush(q, [dis[nv], nv])

dis1 = [INF]*n
dis1[n-1] = 0

q = []
heapq.heapify(q)
# (0からのdis, 頂点番号)
heapq.heappush(q, [0, n-1])
while len(q) > 0:
    d, v = heapq.heappop(q)
    if dis1[v] < d:
        continue
    for nv, c in g[v]:
        if dis1[nv] > dis1[v]+c:
            dis1[nv] = dis1[v]+c
            heapq.heappush(q, [dis1[nv], nv])

for i in range(n):
    print(dis[i]+dis1[i])
