# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from copy import deepcopy
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = []

for i in range(n):
    ai = list(input())
    a.append(ai)

b = deepcopy(a)

for i in range(n-1):
    b[0][i+1] = a[0][i]

for j in range(n-1):
    b[j+1][n-1] = a[j][n-1]

for i in range(1, n):
    b[n-1][i-1] = a[n-1][i]

for j in range(1, n):
    b[j-1][0] = a[j][0]


for i in range(n):
    print(*b[i], sep="")
