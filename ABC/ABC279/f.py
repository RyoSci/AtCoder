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

    def union(self, x, y, is_ball):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
            ufid2boxid[x], ufid2boxid[y] = ufid2boxid[y], ufid2boxid[x]
            boxid2ufid[ufid2boxid[x]], boxid2ufid[ufid2boxid[y]
                                                  ] = boxid2ufid[ufid2boxid[y]], boxid2ufid[ufid2boxid[x]]

        # 各要素も持つ場合
        if is_ball:
            for i in self.group[y]:
                self.parents[i] = x
                self.group[x].append(i)
            self.group[y] = [self.group[y][0]]

            self.parents[x] = -len(self.group[x])
            self.parents[y] = x
        else:
            for i in self.group[y][1:]:
                self.parents[i] = x
                self.group[x].append(i)
            self.group[y] = [self.group[y][0]]

            self.parents[x] = -len(self.group[x])
            self.parents[y] = -1

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


n, q = map(int, input().split())
boxid2ufid = list(range(n))
ufid2boxid = list(range(n))
uf = UnionFind(n+n+q)
cnt = n
ans = []
for i in range(n):
    uf.union(i, i+n, True)

for i in range(q):
    op = list(map(int, input().split()))
    num = op[0]
    if num == 1:
        x, y = op[1:]
        x -= 1
        y -= 1
        uf.union(boxid2ufid[x], boxid2ufid[y], False)
    elif num == 2:
        x = op[1]
        x -= 1
        uf.union(boxid2ufid[x], cnt+n, True)
        cnt += 1
    else:
        x = op[1]
        x -= 1
        tmp = uf.find(x+n)
        ans.append(ufid2boxid[tmp]+1)

print(*ans)
