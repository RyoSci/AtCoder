# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

b = list(set(a))
b.sort()


for i in range(n):
    dis = bisect_left(b, a[i])
    print(dis+1)
