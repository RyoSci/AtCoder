# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left, bisect_right
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, q = map(int, input().split())
a = list(map(int, input().split()))
a = [0]+a
a.sort()
x = [int(input()) for _ in range(q)]

a_tot = [0]*(n+1)
for i in range(n):
    a_tot[i+1] += a[i+1]+a_tot[i]

a_tot += [INF]
ans = []
for i in range(q):
    r = bisect_right(a, x[i])
    l = bisect_left(a, x[i])
    if a_tot[l] == INF:
        res = x[i]*n-a_tot[n]
    elif l == 0:
        res = a_tot[n]-x[i]*n
    else:
        res = a_tot[n]-a_tot[r-1]-(n-r+1)*x[i]
        res += (l-1)*x[i]-(a_tot[l-1]-a_tot[0])
    ans.append(res)

print(*ans, sep="\n")
