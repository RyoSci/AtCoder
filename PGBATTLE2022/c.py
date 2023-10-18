# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_right
import sys
def input(): return sys.stdin.readline().rstrip()


# n, p, q = map(int, input().split())
n = 2*10**5
p = 10**4
q = 10**4

c = []
d = []
for i in range(n):
    # a, b = map(int, input().split())
    a, b = 10**4, 10**4
    res = p*a+q*b
    c.append(res)
    d.append(res)

c.sort()

for i in range(n):
    pos = bisect_right(c, d[i])
    print(n-pos+1)
