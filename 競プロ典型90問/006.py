
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

"https://judge.yosupo.jp/submission/7795"


class SegTree:
    X_unit = "z"
    X_f = min

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f([self.X[i << 1], self.X[i << 1 | 1]])
            # self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def add_val(self, i, x):
        i += self.N
        self.X[i] += x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f([self.X[i << 1], self.X[i << 1 | 1]])
            # self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        # vL = self.X_unit
        # vR = self.X_unit
        L_min_index = L
        R_min_index = R
        while L < R:
            if L & 1:
                if self.X[L_min_index] > self.X[L]:
                    L_min_index = L
                # vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                # vR = self.X_f(self.X[R], vR)
                if self.X[R_min_index] > self.X[R]:
                    R_min_index = R
            L >>= 1
            R >>= 1
        # print(L_min_index, R_min_index, "AAA")
        if self.X[L_min_index] <= self.X[R_min_index]:
            return L_min_index
        else:
            return R_min_index

        # return self.X_f(vL, vR)


N, K = map(int, readline().split())
N_ = N
i = 0
while 1:
    if N_ <= 2**i:
        N_ = 2**i
        break
    i += 1
S = input().strip()

seg = SegTree(N_)
seg.build(S)
# print(seg.X)


def f(l, a):
    while 1:
        if N_ <= l < 2*N_:
            break
        if seg.X[2*l] == a:
            l = 2*l
        else:
            l = 2*l+1
    return l-N_


ans = []
l = 0
for r in range(N-K, N):
    print(seg.X[l+N_], seg.X[r+N_])
    l = seg.fold(l, r)
    a = seg.X[l]
    ans.append(seg.X[l])
    l = f(l, a)+1
    # print(ans)


print(*ans, sep="")
