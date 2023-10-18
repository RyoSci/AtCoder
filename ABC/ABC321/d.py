# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_right
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

b_tot = [0]*(m+1)
for i in range(m):
    b_tot[i+1] += b_tot[i] + b[i]


ans = 0
for i in range(n):
    bi = p - a[i]

    pos = bisect_right(b, bi)

    res = a[i] * pos + b_tot[pos] + p*(m-pos)
    ans += res

print(ans)
