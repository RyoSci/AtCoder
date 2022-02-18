from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

INF = 10 ** 18


def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        d, v = heappop(hq)  # ノードを pop する
        if dist[v] < d:
            continue
        seen[v] = True
        for to, cost, k in adj[v]:  # ノード v に隣接しているノードに対して
            start = (dist[v]+(k-1))//k*k
            if seen[to] == False and start + cost < dist[to]:
                # if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = start + cost
                # dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


# ノード数, エッジ数, 始点ノード
n, m, x, y = map(int, input().split())
# v, e, r = map(int, input().split())
# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(n)]
# adj = [[] for _ in range(v)]
for i in range(m):
    # for i in range(e):
    a, b, t, k = map(int, input().split())
    # s, t, d = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append((b, t, k))
    adj[b].append((a, t, k))
    # adj[s].append((t, d))

d = dijkstra(x-1, n)
if d[y-1] == INF:
    print(-1)
else:
    print(d[y-1])
