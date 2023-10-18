from re import template


# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b, c = list(map(int, input().split()))
if a <= b and b <= c or a >= b and b >= c:
    print("Yes")
else:
    print("No")
