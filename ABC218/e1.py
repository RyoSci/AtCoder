from collections import defaultdict
from heapq import heappush, heappop, heapify
import heapq
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

"https: // note.nkmk.me/python-union-find/"


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


s = 0
N, M = map(int, input().split())
G = [[] for _ in range(M)]
for i in range(M):
    a, b, c = map(int, input().split())
    if a > b:
        a, b = b, a
    G[i] = [c, a-1, b-1]
    s += c
G.sort()

uf = UnionFind(N)

used = [0]*M
cost = [0]*M
# ans = 0
for i in range(M):
    w = G[i][0]
    u = G[i][1]
    v = G[i][2]
    cost[i] = w
    if uf.same(u, v):
        continue
    used[i] = 1
    # ans += w
    uf.union(u, v)


ans = 0
for i in range(M):
    if used[i] == 1:
        continue
    else:
        if cost[i] >= 0:
            ans += cost[i]


print(ans)
# print(used)
# print(cost)
