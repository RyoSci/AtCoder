import sys
from collections import defaultdict
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

        # # 代表源ごとに所属する各要素も持つ場合
        # self.group = [[i] for i in range(n)]

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

        # # 代表源ごとに所属する各要素も持つ場合
        # self.group[x] += self.group[y]
        # self.group[y] = []

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # def members2(self, x):
    #     """
    #     代表源ごとに所属する各要素も持つ場合
    #     所属する要素を数えるのにmembers関数より早い
    #     """
    #     root = self.find(x)
    #     return self.group[root]

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


n, m = map(int, input().split())
uf = UnionFind(n)
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uf.union(u, v)

k = int(input())
ngs = set()
for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    px = uf.find(x)
    py = uf.find(y)
    tmp = [px, py]
    tmp.sort()
    ngs.add(tuple(tmp))

q = int(input())
for i in range(q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    px = uf.find(p)
    py = uf.find(q)
    tmp = [px, py]
    tmp.sort()

    if tuple(tmp) in ngs:
        print("No")
    else:
        print("Yes")
