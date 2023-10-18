# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from math import sin, cos, pi
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())

rx = (x0+xn2)/2
ry = (y0+yn2)/2

x0 -= rx
y0 -= ry

z = x0+1j*y0

z *= (cos(2*pi/n) + 1j*sin(2*pi/n))

print(z.real + rx, z.imag+ry)
