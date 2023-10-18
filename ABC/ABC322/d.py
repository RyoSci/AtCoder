# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from copy import deepcopy
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


p = []
for k in range(3):
    tmp = []
    for i in range(4):
        pi = input()
        tmp.append(list(pi))
    p.append(tmp)


def rotate(S, k=1):
    for _ in range(k):
        ans = [['']*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                ans[j][4-1-i] = S[i][j]
        S = ans
    return S


def serch(S):
    u = INF
    d = -1
    l = INF
    r = -1

    for i in range(4):
        for j in range(4):
            if S[i][j] == "#":
                u = min(u, i)
                d = max(d, i)

                l = min(l, j)
                r = max(r, j)

    return u, r, d, l


u0, r0, d0, l0 = serch(p[0])
g = [[0]*(4) for _ in range(4)]


def move(g, S, i, j, u, r, d, l):
    gg = deepcopy(g)
    for i0 in range(u, d+1):
        for j0 in range(l, r+1):
            ni = i + i0 - u
            nj = j + j0 - l
            if 0 <= ni < 4 and 0 <= nj < 4:
                if S[i0][j0] == "#":
                    if gg[ni][nj] == 1:
                        return False
                    else:
                        gg[ni][nj] = 1
                else:
                    continue
            else:
                return False
    return gg


for i in range(4):
    for j in range(4):

        if move(g, p[0], i, j, u0, r0, d0, l0):
            g0 = move(g, p[0], i, j, u0, r0, d0, l0)
        else:
            continue

        for k in range(4):
            p1 = rotate(p[1], k)
            u1, r1, d1, l1 = serch(p1)
            for i1 in range(4):
                for j1 in range(4):
                    if move(g0, p1, i1, j1, u1, r1, d1, l1):
                        g1 = move(g0, p1, i1, j1, u1, r1, d1, l1)
                    else:
                        continue

                    for kk in range(4):
                        p2 = rotate(p[2], kk)
                        u2, r2, d2, l2 = serch(p2)
                        for i2 in range(4):
                            for j2 in range(4):
                                if move(g1, p2, i2, j2, u2, r2, d2, l2):
                                    g2 = move(g1, p2, i2, j2, u2, r2, d2, l2)
                                else:
                                    continue
                                ans = True
                                for i3 in range(4):
                                    for j3 in range(4):
                                        if g2[i3][j3] == 0:
                                            ans = False
                                            break
                                    if not ans:
                                        break
                                if ans:
                                    print("Yes")
                                    exit()
else:
    print("No")
