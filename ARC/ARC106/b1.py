import collections
import itertools
import operator


class UnionFind:
    def __init__(self, elems=None):
        class KeyDict(dict):
            def __missing__(self, key):
                self[key] = key
                return key

        self.parent = KeyDict()
        self.rank = collections.defaultdict(int)

        if elems is not None:
            for elem in elems:
                _, _ = self.parent[elem], self.rank[elem]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def are_same(self, x, y):
        return self.find(x) == self.find(y)

    def grouper(self):
        roots = [(x, self.find(x_par)) for x, x_par in self.parent.items()]
        root = operator.itemgetter(1)
        for _, group in itertools.groupby(sorted(roots, key=root), root):
            yield [x for x, _ in group]


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

uf = UnionFind()
for i in range(m):
    c, d = map(int, input().split())
    uf.unite(c - 1, d - 1)

group = list(uf.grouper())
for i in group:
    tmp = 0
    for j in i:
        tmp += b[j] - a[j]
    if tmp != 0:
        print("No")
        break
else:
    print("Yes")

print(group)
