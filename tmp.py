import sys


class LazySegmentTree():
    def __init__(self, n, op, e, mapping, composition, id):
        self.n = n
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.data = [e] * (2 * self.size)
        self.lazy = [id] * (self.size)

    def update(self, k):
        self.data[k] = self.op(self.data[2 * k], self.data[2 * k + 1])

    def all_apply(self, k, f):
        self.data[k] = self.mapping(f, self.data[k])
        if k < self.size:
            self.lazy[k] = self.composition(f, self.lazy[k])

    def push(self, k):  # 親の遅延配列の値を子に反映させる
        self.all_apply(2 * k, self.lazy[k])
        self.all_apply(2 * k + 1, self.lazy[k])
        self.lazy[k] = self.id

    def build(self, arr):
        #assert len(arr) == self.n
        for i, a in enumerate(arr):
            self.data[self.size + i] = a
        for i in range(self.size-1, 0, -1):
            self.update(i)

    def set(self, p, x):
        #assert 0 <= p < self.n
        p += self.size
        # 事前に関係のある遅延配列を全て反映させてしまう
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = x  # 値を更新する
        # 関係のある区間の値も更新する
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        #assert 0 <= p < self.n
        p += self.size
        # 関係のある遅延配列を全て反映させる
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.data[p]

    def prod(self, l, r):
        #assert 0 <= l <= r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push(r >> i)
        sml = smr = self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.data[1]

    def apply(self, p, f):
        #assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = self.mapping(f, self.data[p])
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def range_apply(self, l, r, f):
        #assert 0 <= l <= r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push((r - 1) >> i)
        l2 = l
        r2 = r
        while l < r:
            if l & 1:
                self.all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.all_apply(r, f)
            l >>= 1
            r >>= 1
        l = l2
        r = r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self.update(l >> i)
            if ((r >> i) << i) != r:
                self.update((r - 1) >> i)

    def max_right(self, l, g):
        #assert 0 <= l <= self.n
        #assert g(self.e)
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self.push(l >> i)
        sm = self.e
        while True:
            while l % 2 == 0:
                l >>= 1
            if not g(self.op(sm, self.data[l])):
                while l < self.size:
                    self.push(l)
                    l = 2 * l
                    if g(self.op(sm, self.data[l])):
                        sm = self.op(sm, self.data[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.data[l])
            l += 1
            if (l & -l) == l:
                return self.n

    def min_left(self, r, g):
        #assert 0 <= r <= self.n
        #assert g(self.e)
        if r == 0:
            return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self.push((r - 1) >> i)
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not g(self.op(self.data[r], sm)):
                while r < self.size:
                    self.push(r)
                    r = 2 * r + 1
                    if g(self.op(self.data[r], sm)):
                        sm = self.op(self.data[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.data[r], sm)
            if (r & -r) == r:
                return 0


input = sys.stdin.readline

INF = 10**18


def op(x, y):
    return x ^ y


def mapping(p, x):  # pが作用素, xが更新する前の値
    if p == INF:
        return x
    return p ^ x


def composition(p, q):  # pをqに作用させる(q,pの順に作用)
    return p ^ q


e = 0
id = 0
N, Q = map(int, input().split())
A = list(map(int, input().split()))

lst = LazySegmentTree(N, op, e, mapping, composition, id)
lst.build(A)

for i in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        lst.apply(x-1, y)
    else:
        print(lst.prod(x-1, y))


sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2(): return list(map(int, sys.stdin.readline().rstrip()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())


class LazySegTree():  # モノイドに対して適用可能、Nが2冪でなくても良い
    def __init__(self, N, X_func, A_func, operate, X_unit, A_unit):
        self.N = N
        self.X_func = X_func
        self.A_func = A_func
        self.operate = operate
        self.X_unit = X_unit
        self.A_unit = A_unit
        self.X = [self.X_unit]*(2*self.N)
        self.A = [self.A_unit]*(2*self.N)
        self.size = [0]*(2*self.N)

    def build(self, init_value):  # 初期値を[N,2N)に格納
        for i in range(self.N):
            self.X[self.N+i] = init_value[i]
            self.size[self.N+i] = 1
        for i in range(self.N-1, 0, -1):
            self.X[i] = self.X_func(self.X[i << 1], self.X[i << 1 | 1])
            self.size[i] = self.size[i << 1] + self.size[i << 1 | 1]

    def update(self, i, x):  # i番目(0-index)の値をxに変更
        i += self.N
        self.X[i] = x
        i >>= 1
        while i:
            self.X[i] = self.X_func(self.X[i << 1], self.X[i << 1 | 1])
            i >>= 1

    def eval_at(self, i):  # i番目で作用を施した値を返す
        return self.operate(self.X[i], self.A[i], self.size[i])

    def eval_above(self, i):  # i番目より上の値を再計算する
        i >>= 1
        while i:
            self.X[i] = self.X_func(self.eval_at(
                i << 1), self.eval_at(i << 1 | 1))
            i >>= 1

    def propagate_at(self, i):  # i番目で作用を施し、1つ下に作用の情報を伝える
        self.X[i] = self.operate(self.X[i], self.A[i], self.size[i])
        self.A[i << 1] = self.A_func(self.A[i << 1], self.A[i])
        self.A[i << 1 | 1] = self.A_func(self.A[i << 1 | 1], self.A[i])
        self.A[i] = self.A_unit

    def propagate_above(self, i):  # i番目より上で作用を施す
        H = i.bit_length()
        for h in range(H, 0, -1):
            self.propagate_at(i >> h)

    def fold(self, L, R):  # [L,R)の区間取得
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self.propagate_above(L0)
        self.propagate_above(R0)
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_func(vL, self.eval_at(L))
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_func(self.eval_at(R), vR)
            L >>= 1
            R >>= 1
        return self.X_func(vL, vR)

    def operate_range(self, L, R, x):  # [L,R)にxを作用
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self.propagate_above(L0)
        self.propagate_above(R0)
        while L < R:
            if L & 1:
                self.A[L] = self.A_func(self.A[L], x)
                L += 1
            if R & 1:
                R -= 1
                self.A[R] = self.A_func(self.A[R], x)
            L >>= 1
            R >>= 1
        self.eval_above(L0)
        self.eval_above(R0)


def X_func(x, y):
    return x ^ y


def A_func(a, b):
    return a ^ b


def operate(x, a, r):  # 右作用
    return x ^ a


X_unit = 0
A_unit = 0

N, Q = MI()
A = LI()

LST = LazySegTree(N, X_func, A_func, operate, X_unit, A_unit)
LST.build(A)

for _ in range(Q):
    t, x, y = MI()
    if t == 1:
        x -= 1
        s = LST.fold(x, x+1)
        LST.update(x, s ^ y)
    else:
        x -= 1
        y -= 1
        print(LST.fold(x, y+1))
