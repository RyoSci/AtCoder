# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
s = []
for i in range(h):
    si = input()
    s.append(list(si))


def up(i, j):
    res = ""
    pos = []
    for k in range(5):
        ni = i-k
        if 0 <= ni < h:
            res += s[ni][j]
        else:
            res = ""
        pos.append((ni+1, j+1))
    if res == "snuke":
        for k in range(5):
            print(*pos[k])
        exit()


def down(i, j):
    res = ""
    pos = []
    for k in range(5):
        ni = i+k
        if 0 <= ni < h:
            res += s[ni][j]
        else:
            res = ""
        pos.append((ni+1, j+1))
    if res == "snuke":
        for k in range(5):
            print(*pos[k])
        exit()


def right(i, j):
    res = ""
    pos = []
    for k in range(5):
        nj = j+k
        if 0 <= nj < w:
            res += s[i][nj]
        else:
            res = ""
        pos.append((i+1, nj+1))
    if res == "snuke":
        for k in range(5):
            print(*pos[k])
        exit()


def left(i, j):
    res = ""
    pos = []
    for k in range(5):
        nj = j-k
        if 0 <= nj < w:
            res += s[i][nj]
        else:
            res = ""
        pos.append((i+1, nj+1))
    if res == "snuke":
        for k in range(5):
            print(*pos[k])
        exit()


def nanariup(i, j):
    res = ""
    pos = []
    for k in range(5):
        ni = i-k
        nj = j+k
        if 0 <= ni < h and 0 <= nj < w:
            res += s[ni][nj]
        else:
            res = ""
        pos.append((ni+1, nj+1))
    if res == "snuke":
        for k in range(5):
            print(*pos[k])
        exit()


def nanaridw(i, j):
    res = ""
    pos = []
    for k in range(5):
        ni = i+k
        nj = j+k
        if 0 <= ni < h and 0 <= nj < w:
            res += s[ni][nj]
        else:
            res = ""
        pos.append((ni+1, nj+1))
    if res == "snuke":
        for k in range(5):
            print(*pos[k])
        exit()


def nanaledw(i, j):
    res = ""
    pos = []
    for k in range(5):
        ni = i+k
        nj = j-k
        if 0 <= ni < h and 0 <= nj < w:
            res += s[ni][nj]
        else:
            res = ""
        pos.append((ni+1, nj+1))
    if res == "snuke":
        for k in range(5):
            print(*pos[k])
        exit()


def nanaleup(i, j):
    res = ""
    pos = []
    for k in range(5):
        ni = i-k
        nj = j-k
        if 0 <= ni < h and 0 <= nj < w:
            res += s[ni][nj]
        else:
            res = ""
        pos.append((ni+1, nj+1))
    if res == "snuke":
        for k in range(5):
            print(*pos[k])
        exit()


for i in range(h):
    for j in range(w):
        up(i, j)
        down(i, j)
        right(i, j)
        left(i, j)
        nanariup(i, j)
        nanaridw(i, j)
        nanaledw(i, j)
        nanaleup(i, j)
