# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import defaultdict
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a, b = map(int, input().split())

d = defaultdict(int)

for _ in range(n):
    p, q, r, s = map(int, input().split())

    for i in range(p, r+1):
        for j in range(q, s+1):
            d[(i, j)] += 1

mx = max(d.values())
area = 0
for val in d.values():
    if val == mx:
        area += 1

print(mx)
print(area)
