# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

        # 各要素も持つ場合
        self.group = [[i] for i in range(n)]

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

        # 各要素も持つ場合
        self.group[x] += self.group[y]
        self.group[y] = []

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def members2(self, x):
        """
        各要素も持つ場合
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


INF = 10**18

n, m = map(int, input().split())
g = [[] for _ in range(n)]
uf = UnionFind(n)

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uf.union(u, v)
    g[u].append(v)
    g[v].append(u)

one = 0
two = 0
for i in range(n):
    if len(g[i]) == 1:
        one += 1
    elif len(g[i]) == 2:
        two += 1

if uf.group_count() == 1 and one == 2 and two == n-2:
    print("Yes")
else:
    print("No")
