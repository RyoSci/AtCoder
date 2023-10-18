# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from math import sqrt
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18
eps = 1e-8

n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())


def f(r, cx, cy):
    d_max = 0
    for i in range(n):
        d = sqrt((x[i]-cx)**2 + (y[i] - cy)**2)
        d_max = max(d, d_max)

    if d_max - eps > r:
        # if d_max > r:
        return False
    else:
        return True


ans = 800
for i in range(n):
    xi = x[i]
    yi = y[i]
    for j in range(i):
        xj = x[j]
        yj = y[j]

        d = sqrt((xj-xi)**2+(yi-yj)**2)

        xij = (xj-xi)/2
        yij = (yj-yi)/2

        ok = 800
        ng = 0
        # while ng+eps < ok:
        for i in range(300):
            r = (ok+ng)/2

            if r**2 - (d/2)**2 >= 0:
                k = sqrt(r**2 - (d/2)**2)
            else:
                ng = r

            xmc = sqrt(yij**2/(xij**2+yij**2))
            ymc = -sqrt(xij**2/(xij**2+yij**2))
            cx0 = xi + xij + k * xmc
            cy0 = yi + yij + k * ymc

            xmc = -sqrt(yij**2/(xij**2+yij**2))
            ymc = sqrt(xij**2/(xij**2+yij**2))
            cx1 = xi + xij + k * xmc
            cy1 = yi + yij + k * ymc

            if f(r, cx0, cy0) or f(r, cx1, cy1):
                ok = r
            else:
                ng = r

        ans = min(ans, ok)

print(ans)
