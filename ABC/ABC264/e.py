# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
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


n, m, k = map(int, input().split())
uv = []
for i in range(k):
    uvi = list(map(lambda x: int(x)-1, input().split()))
    uv.append(uvi)

q = int(input())
x = []
for i in range(q):
    xi = int(input())
    x.append(xi)

xs = set(x)


uf = UnionFind(n+m)
for i in range(m):
    uf.union(n, n+i)

for i in range(k):
    if i+1 not in xs:
        uf.union(uv[i][0], uv[i][1])

ans = [0]*q
x = x[::-1]
for i in range(q):
    cnt = len(uf.members2(n)) - m
    # print(uf.all_group_members())
    ans[i] = cnt
    tmp = uv[x[i]-1]
    # print(cnt, tmp)
    uf.union(tmp[0], tmp[1])

ans = ans[::-1]
print(*ans)
