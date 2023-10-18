# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import math
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18
eps = 1e-10


a, b = map(int, input().split())

if a > b:
    a, b = b, a

ok = 0
ng = b


def f(x):
    # x1 = -x
    # y1 = a

    # pi = math.acos(-1)
    # rad = 60/180*pi
    # x_rotated = x1 * math.cos(rad) + y1 * math.sin(rad)
    # y_rotated = -x1 * math.sin(rad) + y1 * math.cos(rad)

    z = complex(-x, a)

    pi = math.acos(-1)
    rad = 60/180*pi
    z *= complex(math.cos(rad), -math.sin(rad))
    x_rotated = z.real
    y_rotated = z.imag

    if 0 - eps <= x_rotated + x <= b + eps and 0+eps <= y_rotated <= a + eps:
        return True
    else:
        return False


for i in range(100):
    m = (ok+ng)/2

    if f(m):
        ok = m
    else:
        ng = m

print((ok**2+a**2)**(1/2))
