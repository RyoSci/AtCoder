# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = []
b = []

for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

ng = 0
ok = INF

while ng+1 < ok:
    m = (ng+ok)//2

    cnt = 0
    for i in range(n):
        if a[i] >= m:
            cnt += b[i]

    if cnt <= k:
        ok = m
    else:
        ng = m

print(ok)
