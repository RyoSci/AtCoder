# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from math import cos, pi, sqrt
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b, h, m = map(int, input().split())

alpha = (h+m/60)/12
beta = m/60


alpha = 2*pi*alpha
beta = 2*pi*beta

c = sqrt(a**2+b**2-2*a*b*cos(beta-alpha))
print(c)
