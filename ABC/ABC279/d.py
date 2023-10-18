# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b = map(int, input().split())

t = (2*b/a)**(-2/3) - 1

t = max(0, int(t))
s = max(0, t+1)
r = max(0, t-1)
ans = INF

if t+1 != 0:
    ans = min(ans, a*(t+1)**(-1/2)+b*t)
if s+1 != 0:
    ans = min(ans, a*(s+1)**(-1/2)+b*s)
if r+1 != 0:
    ans = min(ans, a*(r+1)**(-1/2)+b*r)
print(ans)
