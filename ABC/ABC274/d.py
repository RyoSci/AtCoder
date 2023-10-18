# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x, y = map(int, input().split())
a = list(map(int, input().split()))

yoko = []
tate = []
for i in range(n):
    if i % 2 == 0:
        yoko.append(a[i])
    else:
        tate.append(a[i])

m = len(yoko)

# dpx = [[0]*20 for _ in range(m+1)]
dpx = [[0]*20100 for _ in range(m+1)]
dpx[0][0] = 1
dpx[1][yoko[0]] = 1
for i in range(1, m):
    for j in range(-10000, 10001, 1):
        # for j in range(-10, 11, 1):
        if dpx[i][j] == 0:
            continue
        nj0 = j-yoko[i]
        nj1 = j+yoko[i]
        if -10000 <= nj0:
            # if -10 <= nj0:
            dpx[i+1][nj0] = dpx[i][j]
        if nj1 <= 10000:
            # if nj1 <= 10:
            dpx[i+1][nj1] = dpx[i][j]
        # print(i, j, nj0, nj1)

if dpx[m][x] == 0:
    print("No")
    exit()

l = len(tate)


# dpy = [[0]*20 for _ in range(l+1)]
dpy = [[0]*20100 for _ in range(l+1)]
dpy[0][0] = 1
for i in range(l):
    # for j in range(-10, 11, 1):
    for j in range(-10000, 10001, 1):
        if dpy[i][j] == 0:
            continue
        nj0 = j-tate[i]
        nj1 = j+tate[i]
        if -10000 <= nj0:
            # if -10 <= nj0:
            dpy[i+1][nj0] = dpy[i][j]
        if nj1 <= 10000:
            # if nj1 <= 10:
            dpy[i+1][nj1] = dpy[i][j]

if dpy[l][y] == 0:
    print("No")
    exit()

# print(dpx)
# print(dpx[m][x])
# print(dpy)


print("Yes")
