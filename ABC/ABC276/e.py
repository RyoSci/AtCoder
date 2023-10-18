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

        # # 各要素も持つ場合
        # self.group = [[i] for i in range(n)]

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

        # # 各要素も持つ場合
        # self.group[x] += self.group[y]
        # self.group[y] = []

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


h, w = map(int, input().split())
c = []
for i in range(h):
    s = input()
    c.append(s)

for i in range(h):
    for j in range(w):
        if c[i][j] == "S":
            sx = i
            sy = j
            break

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def check(x, y):
    return 0 <= x < h and 0 <= y < w and c[x][y] == "."


uf = UnionFind(h*w)


def cal(x, y):
    return x*w+y


def bfs(nx, ny, px, py):
    q = deque()
    q.append([nx, ny, px, py])
    while len(q) > 0:
        x, y, px, py = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (nx, ny) == (px, py):
                continue
            if check(nx, ny) and not uf.same(cal(x, y), cal(nx, ny)):
                uf.union(cal(x, y), cal(nx, ny))
                q.append([nx, ny, x, y])


def dfs(x, y, px, py):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (nx, ny) == (px, py):
            continue
        if check(nx, ny) and not uf.same(cal(nx, ny), cal(x, y)):
            uf.union(cal(x, y), cal(nx, ny))
            dfs(nx, ny, x, y)


for i in range(4):
    nx = sx+dx[i]
    ny = sy+dy[i]
    if check(nx, ny):
        # bfs(nx, ny, -1, -1)
        dfs(nx, ny, -1, -1)

ans = "No"
for i in range(4):
    xi = sx+dx[i]
    yi = sy+dy[i]
    if not check(xi, yi):
        continue
    for j in range(4):
        if i == j:
            continue
        xj = sx+dx[j]
        yj = sy+dy[j]
        if not check(xj, yj):
            continue
        if uf.same(cal(xi, yi), cal(xj, yj)):
            ans = "Yes"

print(ans)
