# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

a, b = map(int, input().split())
if a**2<b**2:
    print("Yes")
else:
    print("No")