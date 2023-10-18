# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


"https://judge.yosupo.jp/submission/7795"


def X_f(x, y): return x ^ y


class SegTree:
    X_unit = 0

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return X_f(vL, vR)


n, q = map(int, input().split())
a = list(map(int, input().split()))
seg = SegTree(n+1)
seg.build(a)

ans = []
for i in range(q):
    t, x, y = map(int, input().split())

    if t == 1:
        seg.set_val(x-1, seg.fold(x-1, x) ^ y)
    else:
        ans.append((seg.fold(x-1, y)))

print(*ans, sep="\n")
