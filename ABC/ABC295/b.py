# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

r, c = map(int, input().split())
b = []
a = []
for i in range(r):
    bi = input()
    b.append(bi)
    a.append(list(bi))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    for j in range(c):
        if b[i][j] in {".", "#"}:
            continue
        for ii in range(r):
            for jj in range(c):
                if abs(ii-i) + abs(jj - j) <= int(b[i][j]):
                    a[ii][jj] = "."

for i in range(r):
    print("".join(a[i]))
