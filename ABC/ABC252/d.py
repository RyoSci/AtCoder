# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left, bisect_right
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 0
for mid in range(n):
    l = bisect_left(a, a[mid])
    r = bisect_right(a, a[mid])
    ans += l*(n-r)

print(ans)
