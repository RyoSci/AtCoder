# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import defaultdict
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


class UnionFind():
    def __init__(self, n, c):
        self.n = n
        self.parents = [-1] * n

        # 代表源ごとに所属する各要素も持つ場合
        self.group = [[i] for i in range(n)]

        self.Class = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            self.Class[i][c[i]] += 1

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        # 代表源ごとに所属する各要素も持つ場合
        self.group[x] += self.group[y]
        self.group[y] = []

        for key, val in self.Class[y].items():
            self.Class[x][key] += val
        self.Class[y] = defaultdict(int)

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def members2(self, x):
        """
        代表源ごとに所属する各要素も持つ場合
        所属する要素を数えるのにmembers関数より早い
        """
        root = self.find(x)
        return self.group[root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


n, q = map(int, input().split())
c = list(map(lambda x: int(x) - 1, input().split()))
uf = UnionFind(n, c)
for _ in range(q):
    i, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if i == 1:
        uf.union(a, b)
    else:
        print(uf.Class[uf.find(a)][b])
