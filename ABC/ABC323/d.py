# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from heapq import *
from collections import defaultdict
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

q = []
heapify(q)
d = defaultdict(int)

for i in range(n):
    s, c = map(int, input().split())
    d[s] += c
    heappush(q, s)

while len(q):
    s = heappop(q)
    c = d[s]
    d[s] = 0

    while c:
        if c % 2 == 1:
            if s not in d:
                heappush(q, s)
            d[s] += 1

        s *= 2
        c //= 2

ans = sum(d.values())
print(ans)
