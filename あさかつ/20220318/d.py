# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF=10**18

from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()

ans = 0
for bb in b:
    u=bisect_left(a,bb)
    d=n-bisect_right(c,bb)
    ans+=u*d

print(ans)