from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n)]
indeg = [0]*n
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    indeg[b] += 1

p = []
for i in range(n):
    if indeg[i] == 0:
        heappush(p, i)

ans = []
while len(p) > 0:
    v = heappop(p)
    ans.append(v+1)
    for i in g[v]:
        indeg[i] -= 1
        if indeg[i] == 0:
            heappush(p, i)

if len(ans) == n:
    print(*ans)
else:
    print(-1)
