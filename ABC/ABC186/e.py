# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


"https://tjkendev.github.io/procon-library/python/math/gcd.html"

# Euclidean Algorithm


def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n

# Euclidean Algorithm (non-recursive)


def gcd2(m, n):
    while n:
        m, n = n, m % n
    return m

# Extended Euclidean Algorithm


def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

# lcm (least common multiple)


def lcm(m, n):
    return m//gcd(m, n)*n


def f(m, x, y):
    c = y + k*m
    d = x + n*m

    return c > 0 and d > 0


def cal(x, y):
    l = -INF
    r = INF

    while l + 1 < r:
        m = (l+r)//2

        if f(m, x, y):
            r = m
        else:
            l = m
    return x + n*r


ans = []
t = int(input())
for _ in range(t):
    n, s, k = map(int, input().split())
    g, x, y = extgcd(k, -n)

    if s % g != 0:
        ans.append(-1)
    else:
        n //= abs(g)
        s //= abs(g)
        k //= abs(g)
        res = cal(s*x, s*y)
        ans.append(res)

print(*ans, sep="\n")
