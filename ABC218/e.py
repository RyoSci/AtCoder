from __future__ import print_function
from heapq import heappush, heappop, heapify
import heapq
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

"https://tjkendev.github.io/procon-library/python/graph/min_st_prim.html"

s = 0
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    if a > b:
        a, b = b, a
    G[a-1].append([b-1, c])
    # G[b-1].append([a-1, c])
    s += c

used = [0]*N
que = [(c, w) for w, c in G[0]]
used[0] = 1
heapify(que)

ans = 0
while que:
    cv, v = heappop(que)
    if used[v]:
        continue
    used[v] = 1
    ans += cv
    for w, c in G[v]:
        if used[w]:
            continue
        heappush(que, (c, w))

print(ans)
print(s-ans)
print(G)
