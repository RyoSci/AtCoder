# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, i))
    g[b].append((a, i))

seen = [0]*n
used = [0]*m


q = deque()
for i in range(n):
    if seen[i]:
        continue
    q.append(i)
    seen[i] = 1
    while len(q):
        par = q.popleft()
        for chi, j in g[par]:
            if seen[chi]:
                continue
            seen[chi] = 1
            used[j] = 1
            q.append(chi)

ans = 0
for i in range(m):
    if used[i] == 0:
        ans += 1

print(ans)
