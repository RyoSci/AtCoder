# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b = map(int, input().split())
c = (a**2+b**2)**(0.5)

print(a/c, b/c)
