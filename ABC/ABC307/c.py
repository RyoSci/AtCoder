# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

ha, wa = map(int, input().split())
a = [list(input()) for _ in range(ha)]

hb, wb = map(int, input().split())
b = [list(input()) for _ in range(hb)]

hx, wx = map(int, input().split())
x = [list(input()) for _ in range(hx)]


def f(h, w, abx):
    black = []
    for i in range(h):
        for j in range(w):
            if abx[i][j] == "#":
                black.append((i, j))

    l, u = black[0]
    return l, u, black


al, au, ab = f(ha, wa, a)
bl, bu, bb = f(hb, wb, b)
xl, xu, xb = f(hx, wx, x)


def g(l, u, i, j, abx):
    di = i-l
    dj = j-u
    for ai, aj in abx:
        ni = ai+di
        nj = aj+dj
        if 0 <= ni < hx and 0 <= nj < wx and x[ni][nj] == "#":
            xx[ni][nj] = "#"
        else:
            return False

    return True


for i, j in xb:
    for ii, jj in xb:
        xx = [["."]*wx for _ in range(hx)]

        if g(al, au, i, j, ab) and g(bl, bu, ii, jj, bb) and x == xx:
            print("Yes")
            exit()

print("No")
