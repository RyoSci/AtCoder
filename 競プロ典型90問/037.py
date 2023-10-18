# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

w, n = map(int, input().split())
lrv = [list(map(int, input().split())) for _ in range(n)]

"https://judge.yosupo.jp/submission/7795"


class SegTree:
    # X_unit = 1 << 30
    # X_f = min
    X_unit = -1
    X_f = max

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            # self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])
            if self.X[i << 1] < self.X[i << 1 | 1]:
                self.X[i] = self.X[i << 1 | 1]
            else:
                self.X[i] = self.X[i << 1]

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            # self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])
            if self.X[i << 1] < self.X[i << 1 | 1]:
                self.X[i] = self.X[i << 1 | 1]
            else:
                self.X[i] = self.X[i << 1]

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                if vL < self.X[L]:
                    vL = self.X[L]
                # vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                if vR < self.X[R]:
                    vR = self.X[R]
                # vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        if vL < vR:
            return vR
        else:
            return vL

        # return self.X_f(vL, vR)


seg = SegTree(w+1)
# 1次元にできたのでコメントアウト
# seg = [SegTree(w+1) for _ in range(n+1)]

seg.set_val(0, 0)
# seg[0].set_val(0, 0)

for i in range(n):
    l, r, v = lrv[i]
    for j in range(w, -1, -1):
        # vv = seg[i].fold(j, j+1)
        # seg[i+1].set_val(j, vv)
        sta = j-r
        end = j-l
        if end >= 0:
            if sta < 0:
                sta = 0
            tmp = seg.fold(sta, end+1)
            # tmp = seg[i].fold(sta, end+1)
            if tmp >= 0:
                vv = v + tmp
                if vv < seg.fold(j, j+1):
                    continue
                seg.set_val(j, vv)
                # vv = max(vv, seg[i+1].fold(j, j+1))
                # seg[i+1].set_val(j, vv)


print(seg.fold(w, w+1))
# print(seg[n].fold(w, w+1))
