# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import cmath
from math import sqrt
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]

# 半径
r = 10**4

ans = []


def same_distance():
    """
    等間隔
    """
    dx = 2*r//50
    dy = 2*r//50
    now_x = -r
    now_y = -r
    y0 = 10**9
    y1 = -10**9
    x0 = 10**9
    x1 = -10**9
    # 経線を引く
    for i in range(50):
        now_x += dx
        ans.append((now_x, y0, now_x, y1))

    # 緯線を引く
    for i in range(50):
        now_y += dy
        ans.append((x0, now_y, x1, now_y))

    print(len(ans))
    for i in ans:
        print(*i)


# same_distance()


def ver_vs_hor(p, q):
    """
    等配分
    """
    dx = 2*r//p
    dy = 2*r//q
    now_x = -r
    now_y = -r
    y0 = 10**9
    y1 = -10**9
    x0 = 10**9
    x1 = -10**9
    # 経線を引く
    for i in range(p):
        now_x += dx
        ans.append((now_x, y0, now_x, y1))

    # 緯線を引く
    for i in range(q):
        now_y += dy
        ans.append((x0, now_y, x1, now_y))

    ans.append((r, r, 0, 0))
    ans.append((-r, r, 0, 0))

    print(len(ans))
    for i in ans:
        print(*i)


# ver_vs_hor(90, 8)


def ver_vs_hor_rot(p, q):
    """
    等配分
    """
    dx = 2*r//p
    dy = 2*r//q
    now_x = -r
    now_y = -r
    y0 = 10**4
    y1 = -10**4
    x0 = 10**4
    x1 = -10**4
    # 経線を引く
    for i in range(p):
        now_x += dx
        ans.append((now_x, y0, now_x, y1))

    # 緯線を引く
    for i in range(q):
        now_y += dy
        ans.append((x0, now_y, x1, now_y))

    ans.append((r, r, 0, 0))
    ans.append((-r, r, 0, 0))

    ans_rot = []
    rot = complex(1/2, sqrt(3)/2)
    for i in range(len(ans)):
        px, py, qx, qy = ans[i]
        c0 = complex(px, py)
        c0 = c0*rot

        c1 = complex(qx, qy)
        c1 = c1*rot

        px = int(c0.real)
        py = int(c0.imag)
        qx = int(c1.real)
        qy = int(c1.imag)

        ans_rot.append((px, py, qx, qy))

    print(len(ans_rot))
    for i in ans_rot:
        print(*i)


bef = 0
aft = 0
for i in range(4):
    bef += a[i]

for i in range(6, 10):
    aft += a[i]

if bef < aft:
    ver_vs_hor_rot(92, 6)
else:
    ver_vs_hor_rot(91, 7)
