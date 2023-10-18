# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
g = dict()

for i in range(n):
    a, b = map(int, input().split())
    if a not in g:
        g[a] = []
    if b not in g:
        g[b] = []
    g[a].append(b)
    g[b].append(a)


q = deque()
q.append(1)

ans = 1

seen = set()
seen.add(1)

while len(q) > 0:
    x = q.popleft()
    ans = max(ans, x)
    if x not in g:
        continue
    for nx in g[x]:
        if nx not in seen:
            seen.add(nx)
            q.append(nx)

print(ans)
