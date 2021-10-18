from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e, r = map(int, input().split())
g = [[] for _ in range(v)]

for i in range(e):
    s, t, d = map(int, input().split())
    g[s].append([t, d])

q = []
heappush(q, [0, r])
INF = 10**18
dis = [INF]*v
dis[r] = 0

while len(q) > 0:
    d, s = heappop(q)
    if d > dis[s]:
        continue
    for t, c in g[s]:
        if d+c < dis[t]:
            dis[t] = d+c
            heappush(q, [dis[t], t])

for i in range(v):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])
