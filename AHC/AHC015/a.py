# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from copy import deepcopy
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = 10
board = [[0]*n for _ in range(n)]


def move(x):
    if x == "L":
        for i in range(n):
            k = 0
            for j in range(n):
                if board[i][j] != 0:
                    board[i][k] = board[i][j]
                    if k != j:
                        board[i][j] = 0
                    k += 1

    elif x == "R":
        for i in range(n):
            k = n-1
            for j in range(n-1, -1, -1):
                if board[i][j] != 0:
                    board[i][k] = board[i][j]
                    if k != j:
                        board[i][j] = 0
                    k -= 1
    if x == "F":
        for j in range(n):
            k = 0
            for i in range(n):
                if board[i][j] != 0:
                    board[k][j] = board[i][j]
                    if k != i:
                        board[i][j] = 0
                    k += 1
    if x == "B":
        for j in range(n):
            k = n-1
            for i in range(n-1, -1, -1):
                if board[i][j] != 0:
                    board[k][j] = board[i][j]
                    if k != i:
                        board[i][j] = 0
                    k -= 1


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


def score():
    uf = UnionFind((n-1)*n+n)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                continue
            for di, dj in [(1-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni = i+di
                nj = j+dj
                if 0 <= ni < n and 0 <= nj < n:
                    if board[i][j] == board[ni][nj]:
                        uf.union(i*n+j, ni*n+nj)

    bunshi = 0
    bunbos = [0]*4
    gm = uf.all_group_members()
    for key, vals in gm.items():
        i, j = key//n, key % n
        if board[i][j] == 0:
            continue
        bunshi += len(vals)**2
        bunbos[board[i][j]] += len(vals)

    bunbo = 0
    for i in range(1, 4):
        bunbo += bunbos[i]**2

    if bunbo == 0:
        return 0

    res = 10**6 * bunshi / bunbo
    return res


a = list(map(int, input().split()))
# cnt = [0]*3

# for i in range(100):
#     cnt[a[i]-1] += 1

# tmp = []
# for i in range(3):
#     tmp.append((cnt[i], i))

# tmp.sort()
# most = tmp[-1][-1]

FRBL = "FRBL"

ans = []
for i in range(100):
    pre = deepcopy(board)
    t = int(input())
    results = []
    for r in range(4):
        ni, nj = t//n, t % n
        board = deepcopy(pre)
        board[ni][nj] = a[i]
        move(FRBL[r])
        tmp_score = score()
        results.append((tmp_score, r))

    results.sort(reverse=True)
    # print(results)
    r = results[0][-1]
    move(FRBL[r])
    print(FRBL[r], flush=True)

#     ans.append(FRBL[r])

# print("AA")
# print(*ans, sep="\n")
