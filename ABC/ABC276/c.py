# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
p = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if p[i-1] > p[i]:
        pos = i
        break

q = p[pos:]
q.sort()

c = bisect_left(q, p[pos-1])
d = p[pos-1]

p[pos-1] = q[c-1]
q[c-1] = d
q.sort(reverse=True)

p[pos:] = q

print(*p)
