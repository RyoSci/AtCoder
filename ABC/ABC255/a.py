# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

r,c  = map(int, input().split())
a=[input().split() for i in range(2)]
print(a[r-1][c-1])