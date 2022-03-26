# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b, c, d = list(map(int, input().split()))

e = (a*60+b)*60
f = (c*60+d)*60+1

if e <= f:
    print("Takahashi")
else:
    print("Aoki")
