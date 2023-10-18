# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

x = list(map(int, input()))
xn = len(x)
m = int(input())

d = 0
for i in x:
    d = max(d, i)


def f(n):
    res = 0
    for i in range(xn-1, -1, -1):
        res += x[i]*pow(n, xn-1-i)
        if res > m:
            return False
    return res <= m


if len(x) == 1:
    if x[0] <= m:
        print(1)
    else:
        print(0)
elif not f(d+1):
    print(0)
else:
    ok = d+1
    ng = INF+10
    while ok+1 < ng:
        mid = (ok+ng)//2
        if f(mid):
            ok = mid
        else:
            ng = mid

    print(ok-d)
