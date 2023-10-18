
import sys
"https://qiita.com/ether2420/items/7b67b2b35ad5f441d686"


def segfunc(x, y):
    return max(x, y)


class LazySegTree_RUQ:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [None]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    def gindex(self, l, r):
        l += self.num
        r += self.num
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[i] = None
            self.lazy[2*i] = v
            self.lazy[2*i+1] = v
            self.tree[2*i] = v
            self.tree[2*i+1] = v

    def set_val(self, l, r, x):
        ids = self.gindex(l, r)
        self.propagates(*self.gindex(l, r))
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r & 1:
                self.lazy[r-1] = x
                self.tree[r-1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    def fold(self, l, r):
        ids = self.gindex(l, r)
        self.propagates(*self.gindex(l, r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res

# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

w, n = map(int, input().split())
lrv = [list(map(int, input().split())) for _ in range(n)]

seg = LazySegTree_RUQ([-1]*(w+1), segfunc, -1)
# 1次元にできたのでコメントアウト
# seg = [SegTree(w+1) for _ in range(n+1)]

seg.set_val(0, 1, 0)
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
                seg.set_val(j, j+1, vv)
                # vv = max(vv, seg[i+1].fold(j, j+1))
                # seg[i+1].set_val(j, vv)


print(seg.fold(w, w+1))
# print(seg[n].fold(w, w+1))
