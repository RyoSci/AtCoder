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


n, m = map(int, input().split())
g = [[] for _ in range(n)]
uf = UnionFind(n)

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    uf.union(u, v)

ans = 0

# 連結じゃないグループを計算
groups = uf.all_group_members()
for key, vals in groups.items():
    ans += (n-len(vals))*len(vals)

# 連結なグループを計算
colors = [-1]*n

for i in range(n):
    if colors[i] != -1:
        continue
    q = deque()
    q.append((i, 0))
    colors[i] = 0
    cnt = [[] for _ in range(2)]
    cnt[0].append(i)
    while len(q) > 0:
        i, mod = q.popleft()
        for ni in g[i]:
            if colors[ni] == -1:
                colors[ni] = (mod+1) % 2
                cnt[(mod+1) % 2].append(ni)
                q.append((ni, (mod+1) % 2))
            elif colors[ni] != -1 and colors[ni] == (mod+1) % 2:
                pass
            elif colors[ni] != -1 and colors[ni] != (mod+1) % 2:
                print(0)
                exit()

    for z in cnt[0]:
        tmp = 0
        for chi in g[z]:
            if colors[chi] != colors[z]:
                tmp += 1
        ans += len(cnt[1]) - tmp
    for z in cnt[1]:
        tmp = 0
        for chi in g[z]:
            if colors[chi] != colors[z]:
                tmp += 1
        ans += len(cnt[0]) - tmp


print(ans//2)
