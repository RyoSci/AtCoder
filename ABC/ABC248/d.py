# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left, bisect_right
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n = int(input())
a = list(map(int, input().split()))
q = int(input())

g = [[] for _ in range(n+1)]
for i in range(n):
    g[a[i]].append(i)

ans = []

for i in range(q):
    l, r, x = map(int, input().split())
    l -= 1
    r -= 1
    ll = bisect_left(g[x], l)
    rr = bisect_right(g[x], r)
    ans.append(rr-ll)


print(*ans, sep="\n")
