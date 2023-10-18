# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
lmax = 0
rmin = INF
for i in range(m):
    l, r = map(int, input().split())
    lmax = max(lmax, l)
    rmin = min(rmin, r)

print(max(0, rmin-lmax+1))
