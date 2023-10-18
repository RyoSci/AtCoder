# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

a, n = map(int, input().split())
m=10**9+7
print(m)
print(pow(a,n,m))