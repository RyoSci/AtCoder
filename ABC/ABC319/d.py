# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
l = list(map(int, input().split()))

ok = INF
ng = 0

while ng+1 < ok:
    mid = (ng+ok)//2

    row = 1
    col = l[0]
    if col <= mid:
        pass
    else:
        row = INF

    for i in range(1, n):
        if col + 1 + l[i] <= mid:
            col = col + 1 + l[i]
        else:
            row += 1
            col = l[i]

        if row > m:
            break

        if col <= mid:
            pass
        else:
            row = INF

    if row <= m and col <= mid:
        ok = mid
    else:
        ng = mid

print(ok)
