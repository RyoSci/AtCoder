# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from heapq import heapify, heappop, heappush
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))
g = [[] for _ in range(n)]
p = [0]*n

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    p[y] += 1

q = []
heapify(q)

dp = [a[i] for i in range(n)]
for i in range(n):
    if p[i] == 0:
        heappush(q, i)


ans = -INF
while len(q) > 0:
    par = heappop(q)
    for chi in g[par]:
        ans = max(ans, a[chi]-dp[par])
        dp[chi] = min(dp[chi], dp[par])
        p[chi] -= 1
        if p[chi] == 0:
            heappush(q, chi)

print(ans)
