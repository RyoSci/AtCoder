# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
n = int(input())
# n = INF


def f(a, b):
    return a**3+(a**2)*b+a*(b**2)+b**3


ans = INF*100
for a in range(10**6+10):
    bl = -1
    br = 10**6 + 10
    while bl+1 < br:
        m = bl+br
        m //= 2
        if f(a, m) >= n:
            ans = min(ans, f(a, m))
            br = m
        else:
            bl = m

print(ans)
