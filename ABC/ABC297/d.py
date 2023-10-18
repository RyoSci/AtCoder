# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b = map(int, input().split())

ans = 0


def gcd(x, y):
    global ans
    if y == 0:
        return
    ans += x//y
    gcd(y, x % y)


if b > a:
    a, b = b, a

gcd(a, b)
print(ans-1)
