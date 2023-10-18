# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from heapq import *
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, s = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    u, v, a, b = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, a, b))
    g[v].append((u, a, b))

c = []
d = []
for i in range(n):
    ci, di = map(int, input().split())
    c.append(ci)
    d.append(di)


hq = []
heapify(hq)
l = 50*50+10
dp = [[INF]*(l) for _ in range(n)]
s = min(s, l-1)
dp[0][s] = 0
heappush(hq, (0, 0, s))

while len(hq):
    t, par, silver = heappop(hq)

    if dp[par][silver] > t:
        continue

    # 換金する
    if dp[par][min(silver+c[par], l-1)] > dp[par][silver]+d[par]:
        dp[par][min(silver+c[par], l-1)] = dp[par][silver]+d[par]
        heappush(hq, (t+d[par], par, min(silver+c[par], l-1)))

    # 進む
    for chi, ai, bi in g[par]:
        if silver-ai >= 0 and dp[chi][min(silver-ai, l-1)] > dp[par][silver]+bi:
            dp[chi][min(silver-ai, l-1)] = dp[par][silver]+bi
            heappush(hq, (t+bi, chi, min(silver-ai, l-1)))

ans = []
for i in range(1, n):
    res = INF
    for j in range(l):
        res = min(res, dp[i][j])
    ans.append(res)

print(*ans)
