# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10 ** 6)
def input(): return sys.stdin.readline().rstrip()


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

        # 代表源ごとに所属する各要素も持つ場合
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

        # 代表源ごとに所属する各要素も持つ場合
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


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(lambda x: int(x)-1, input().split()))

    uf = UnionFind(n)
    p = [set() for _ in range(n)]
    for i in range(n):
        uf.union(i, a[i])
        p[i].add(a[i])
        p[a[i]].add(i)

    cnt = 0
    for i in range(n):
        if len(p[i]) <= 1:
            cnt += 1

    mx = uf.group_count()
    if cnt >= 4:
        mn = mx-cnt//2+1
    else:
        mn = mx

    print(mn, mx)
