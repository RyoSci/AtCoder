# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from heapq import *
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
n = len(a)


hq = []
heapify(hq)

for i in range(n):
    heappush(hq, a[i])

s = set()
ans = []
while len(hq):
    p = heappop(hq)
    if p in s:
        continue
    s.add(p)
    ans.append(p)
    if len(ans) == k:
        break

    for i in range(n):
        heappush(hq, p+a[i])

print(ans[-1])
