# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_right
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
xyz = [[] for _ in range(n+1)]
for i in range(m):
    x, y, z = map(int, input().split())
    xyz[x].append((y, z))

dp = [[0]*n for _ in range(1 << n)]
for i in range(n):
    dp[1 << i][i] = 1


for i in range(1 << n):
    tmp = []
    for j in range(n):
        if i >> j & 1:
            tmp.append(j+1)

    ok = True
    for y, z in xyz[len(tmp)]:
        pos = bisect_right(tmp, y)
        if pos > z:
            ok = False

    if not ok:
        continue

    for node in range(n):
        if dp[i][node] == 0:
            continue
        if ((i >> node) & 1) == 0:
            continue

        for to in range(n):
            if ((i >> to) & 1) == 1:
                continue
            dp[i | (1 << to)][to] += dp[i][node]

ans = 0
for i in range(n):
    ans += dp[(1 << n)-1][i]

print(ans)
