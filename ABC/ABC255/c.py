# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

x, a, d, n = list(map(int, input().split()))


def f(a, d, n):
    return a+d*(n-1)


if d == 0:
    ans = abs(f(a, d, n)-x)
elif d > 0:
    if x <= f(a, d, 1):
        ans = abs(f(a, d, 1)-x)
    elif f(a, d, n) <= x:
        ans = abs(f(a, d, n)-x)
    else:
        l = max(1, (x-a)//d+1)
        r = min(n, (x-a+d-1)//d+1)
        ans = min(abs(f(a, d, r)-x), abs(x-f(a, d, l)))
else:
    if f(a, d, 1) <= x:
        ans = abs(f(a, d, 1)-x)
    elif x <= f(a, d, n):
        ans = abs(f(a, d, n)-x)
    else:
        l = max(1, (x-a)//d+1)
        r = min(n, (x-a+d-1)//d+1)
        ans = min(abs(f(a, d, r)-x), abs(x-f(a, d, l)))

print(ans)
# print(f(a, d, r))
# print(l, r)
