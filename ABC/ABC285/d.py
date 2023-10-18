# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
sd = dict()
td = dict()
g = [[] for _ in range(n)]
p = [0]*n

for i in range(n):
    si, ti = input().split()
    if si in td:
        j = td[si]
        g[i].append(j)
        p[j] += 1

    if ti in sd:
        j = sd[ti]
        g[j].append(i)
        p[i] += 1

    td[ti] = i
    sd[si] = i


q = deque()

for i in range(n):
    if p[i] == 0:
        q.append(i)

while len(q) > 0:
    par = q.popleft()
    for chi in g[par]:
        p[chi] -= 1
        if p[chi] == 0:
            q.append(chi)

if sum(p) == 0:
    print("Yes")
else:
    print("No")
