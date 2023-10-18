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


"https://tjkendev.github.io/procon-library/python/range_query/bit.html"

# Binary Indexed Tree (Fenwick Tree)


class BIT:
    def __init__(self, n):
        self.n = n
        self.n0 = 2**(n-1).bit_length()
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)

    def init(self, A):
        self.data[1:] = A
        for i in range(1, self.n):
            if i + (i & -i) <= self.n:
                self.data[i + (i & -i)] += self.data[i]

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        # assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)

    def lower_bound(self, x):
        w = i = 0
        k = self.n0
        while k:
            if i+k <= self.n and w + self.data[i+k] <= x:
                w += self.data[i+k]
                i += k
            k >>= 1
        # assert self.get(0, i) <= x < self.get(0, i+1)
        return i+1


n = int(input())
a = list(map(int, input().split()))
mod = 998244353

az = dict()
for ai in a:
    az[ai] = 0
m = 1
keys = list(az.keys())
keys.sort()

for key in keys:
    az[key] = m
    m += 1

fw = BIT(m)
two = 1
itwo = 1
ans = 0
for i in range(n):
    r = az[a[i]]
    ans += two*fw.sum(r)
    ans %= mod

    two *= 2
    two %= mod
    # itwo *= pow(2, -1, mod)
    _, x, _ = extgcd(2, mod)
    itwo *= x
    itwo %= mod
    fw.add(r, itwo)

print(ans)
