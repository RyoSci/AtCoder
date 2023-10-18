# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ok = INF
ng = 0

while ng+1 < ok:
    mid = (ok+ng)//2

    ca = 0
    for i in range(n):
        if a[i] <= mid:
            ca += 1
    cb = 0
    for i in range(m):
        if b[i] >= mid:
            cb += 1

    if ca >= cb:
        ok = mid
    else:
        ng = mid

print(ok)
