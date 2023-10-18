# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

w, h = map(int, input().split())
n = int(input())
p = []
q = []
for i in range(n):
    pi, qi = map(int, input().split())
    p.append(pi)
    q.append(qi)

A = int(input())
a = list(map(int, input().split()))

B = int(input())
b = list(map(int, input().split()))


d = dict()
for i in range(n):
    x = bisect_left(a, p[i])
    y = bisect_left(b, q[i])

    if (x, y) not in d:
        d[(x, y)] = 0
    d[(x, y)] += 1

M = 0
m = INF
for val in d.values():
    M = max(M, val)
    m = min(m, val)

if len(d) != (A+1)*(B+1):
    m = 0

print(m, M)
