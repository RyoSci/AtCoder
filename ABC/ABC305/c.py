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

l = INF
r = -INF
u = INF
d = -INF
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            l = min(l, j)
            r = max(r, j)

            u = min(u, i)
            d = max(d, i)


for i in range(u, d+1):
    for j in range(l, r+1):
        if s[i][j] == ".":
            print(i+1, j+1)
            exit()
