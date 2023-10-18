# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


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
        assert i > 0
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


n, q = map(int, input().split())
a = list(map(int, input().split()))

bits = [BIT(n) for _ in range(30)]


def cal(x, i):
    for digit in range(30):
        bits[digit].add(i, x % 2)
        x >>= 1
        if x == 0:
            break


for i in range(n):
    cal(a[i], i+1)

twos = [2**i for i in range(40)]

ans = []
for i in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        cal(y, x)
    else:
        res = 0
        for digit in range(30):
            res += (bits[digit].get(x-1, y)) % 2*twos[digit]
        ans.append(res)


print(*ans, sep="\n")
