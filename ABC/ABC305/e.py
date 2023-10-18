# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from heapq import *
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, k = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


hq = []
heapify(hq)

cnt = [-1]*n
for i in range(k):
    p, h = map(int, input().split())
    p -= 1
    heappush(hq, (-h, p))
    cnt[p] = h

while len(hq):
    h, p = heappop(hq)
    h *= -1

    if cnt[p] > h:
        continue

    for chi in g[p]:
        if cnt[chi] < h-1 and h > 0:
            cnt[chi] = h-1
            heappush(hq, (-(h-1), chi))


ans = []
for i in range(n):
    if cnt[i] != -1:
        ans.append(i+1)

print(len(ans))
print(*ans)
