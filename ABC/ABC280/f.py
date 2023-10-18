# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
from collections import defaultdict
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


n, m, q = map(int, input().split())
uf = UnionFind(n)
g = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, -c))
    uf.union(a, b)

# print(uf.all_group_members())
dis = dict()

for root, vals in uf.all_group_members().items():
    dis[root] = dict()
    dis[root][root] = 0
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        par = queue.popleft()
        for chi, c in g[par]:
            if chi not in dis[root]:
                dis[root][chi] = dis[root][par]+c
                queue.append(chi)
            elif dis[root][chi] != dis[root][par]+c:
                queue.clear()
                dis[root] = INF
                break


ans = []
for i in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if not uf.same(x, y):
        ans.append("nan")
    else:
        root = uf.find(x)
        if dis[root] == INF:
            ans.append("inf")
        else:
            res = dis[root][y] - dis[root][x]
            ans.append(res)
# print(dis)
print(*ans)
