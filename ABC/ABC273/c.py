# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_right
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n = int(input())
a = list(map(int, input().split()))

b = list(set(a))
b.sort()

ans = [0]*n
for i in range(n):
    pos = bisect_right(b, a[i])
    ans[len(b)-pos] += 1

print(*ans)
