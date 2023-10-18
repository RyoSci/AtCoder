# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque, defaultdict
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
c = []
for i in range(h):
    ci = input()
    c.append(list(ci))


rows_map = [defaultdict(int) for _ in range(h)]
columns_map = [defaultdict(int) for _ in range(w)]

for i in range(h):
    for j in range(w):
        rows_map[i][c[i][j]] += 1
        columns_map[j][c[i][j]] += 1

ok = deque()

for i in range(h):
    if len(rows_map[i]) == 1:
        ok.appendleft(0*10**5 + i)

for j in range(w):
    if len(columns_map[j]) == 1:
        ok.append(1*10**5 + j)

# seen_h = [0]*h
# seen_w = [0]*w

while len(ok):
    pos = ok.popleft()
    if pos >= 10**5:
        cat = 1
        pos = pos-10**5
    else:
        cat = 0

    if cat == 0:
        i = pos
        # seen_h[i] = 1
        for j in range(w):
            if c[i][j] == ".":
                continue
            columns_map[j][c[i][j]] -= 1
            if columns_map[j][c[i][j]] == 0:
                del columns_map[j][c[i][j]]
                # and seen_w[j] == 0:
                if len(columns_map[j]) == 1 and list(columns_map[j].values())[0] > 1:
                    ok.append(1*10**5 + j)
            c[i][j] = "."

    else:
        j = pos
        # seen_w[j] = 1
        for i in range(h):
            if c[i][j] == ".":
                continue
            rows_map[i][c[i][j]] -= 1
            if rows_map[i][c[i][j]] == 0:
                del rows_map[i][c[i][j]]
                # and seen_h[i] == 0:
                if len(rows_map[i]) == 1 and list(rows_map[i].values())[0] > 1:
                    ok.appendleft(0*10**5 + i)
            c[i][j] = "."


ans = 0
for i in range(h):
    for j in range(w):
        if c[i][j] != ".":
            ans += 1

# print(*c, sep="\n")
print(ans)
