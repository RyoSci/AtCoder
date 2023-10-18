# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from heapq import *
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
p = list(map(int, input().split()))
l = list(map(int, input().split()))
d = list(map(int, input().split()))


tot = []

for i in range(n):
    tot.append((p[i], 0, i))

for i in range(m):
    tot.append((l[i], -1, i))

tot.sort()

ans = 0


hq = []
heapify(hq)

for i in range(n+m):
    num, cat, ii = tot[i]

    if cat == 0:
        if len(hq):
            top = heappop(hq)
            top *= -1
            ans += num - top
        else:
            ans += num

    else:
        heappush(hq, -d[ii])


print(ans)
