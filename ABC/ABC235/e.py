from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# Union-Find


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

# Code


def main():
    n, m, q = map(int, input().split())
    uf = UnionFind(n)

    edges = []

    for _ in range(m):
        u, v, c = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((c, u, v))

    # 重みが小さい順に辺をソート
    edges.sort()
    INF = 10**18
    pair = [INF]*n

    for edge in edges:
        c, u, v = edge
        # 頂点がつながっていなければ
        if not uf.same(u, v):
            uf.union(u, v)  # 頂点同士をつなげる
            pair[u] = min(pair[u], c)
            pair[v] = min(pair[v], c)

    ans = []
    for i in range(q):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        if u != v and (pair[u] > w or pair[v] > w):
            ans.append("Yes")
        else:
            ans.append("No")

    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
