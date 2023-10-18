# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

g = [[] for _ in range(n)]
rg = [[] for _ in range(n)]
p = [0]*n

for i in range(n):
    ci, *pi = list(map(int, input().split()))
    for pij in pi:
        g[i].append(pij-1)
        rg[pij-1].append(i)

        p[i] += 1


ok = [0]*n


def dfs(par):
    for chi in g[par]:
        if ok[chi]:
            continue
        ok[chi] = 1
        dfs(chi)


ok[0] = 1
dfs(0)


q = deque()

for i in range(n):
    if p[i] == 0 and ok[i]:
        q.append(i)

ans = []
while len(q):
    i = q.popleft()
    ans.append(i+1)
    for chi in rg[i]:
        p[chi] -= 1
        if p[chi] == 0 and ok[chi]:
            q.append(chi)


print(*ans[:-1])
