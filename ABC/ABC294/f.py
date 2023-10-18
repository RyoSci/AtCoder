# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

"https://at274.hatenablog.com/entry/2018/02/03/140504"


class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        # 根への距離を管理
        self.weight = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 併合
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            self.weight[rx] = w
            return

        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


n = int(input())
wuf = WeightedUnionFind(n)
edges = []
for i in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v, w))
    wuf.union(u, v, w)

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, w = query[1:]
        u, v, _ = edges[i]
        wuf.union(u, v, w)
    else:
        u, v = query[1:]
        u -= 1
        v -= 1
        print(wuf.diff(u, v))
