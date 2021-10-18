

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

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
p = list(map(int, input().split()))

uf = UnionFind(2*n)

for i in range(n):
    uf.union(i+n, p[i]-1)

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    # uf.union(x+n, p[x]-1)
    # uf.union(y+n, p[y]-1)
    uf.union(x+n, y+n)


res = 0
for root, members in uf.all_group_members().items():
    s = set()
    t = set()
    for member in members:
        if member >= n:
            s.add(member-n)
        else:
            t.add(member)
    # print(s & t)
    res += len(s & t)

print(res)
# print(uf.parents)
# print(uf.all_group_members())
