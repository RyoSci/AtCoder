# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

s = list(input())
s.sort()
if s==list("abc"):
    print("Yes")
else:
    print("No")
