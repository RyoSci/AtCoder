# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from math import sqrt
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

d = [0]*(n+1)

for i in range(1, n+1):
    for j in range(i, n+1, i):
        d[j] += 1

ans = 0
for cd in range(1, n):
    ab = n-cd

    ans += d[cd] * d[ab]

print(ans)
