# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

ok = INF
ng = -1

while ng+1 < ok:
    m = (ok+ng)//2

    flag = True
    for i in range(1, n):
        if a[0]+m > a[i]:
            pass
        else:
            flag = False

    if flag:
        ok = m
    else:
        ng = m

print(ok)
