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
    tmp = []
    for cij in ci:
        tmp.append(ord(cij)-ord("a"))

    c.append(tmp)


rows_map = [[0]*26 for _ in range(h)]
columns_map = [[0]*26 for _ in range(w)]

for i in range(h):
    for j in range(w):
        rows_map[i][c[i][j]] += 1
        columns_map[j][c[i][j]] += 1

ok = deque()

for i in range(h):
    cnt = 0
    for k in range(26):
        if rows_map[i][k] > 0:
            cnt += 1
    if cnt == 1:
        ok.appendleft(0*10**5 + i)

for j in range(w):
    cnt = 0
    for k in range(26):
        if columns_map[j][k] > 0:
            cnt += 1
    if cnt == 1:
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
            if c[i][j] == -1:
                continue
            columns_map[j][c[i][j]] -= 1
            if columns_map[j][c[i][j]] == 0:
                cnt = 0
                num = -1
                for k in range(26):
                    if columns_map[j][k] > 0:
                        cnt += 1
                        num = columns_map[j][k]
                if cnt == 1 and num > 1:
                    ok.append(1*10**5 + j)
            c[i][j] = -1

    else:
        j = pos
        # seen_w[j] = 1
        for i in range(h):
            if c[i][j] == -1:
                continue
            rows_map[i][c[i][j]] -= 1
            if rows_map[i][c[i][j]] == 0:
                cnt = 0
                num = -1
                for k in range(26):
                    if rows_map[i][k] > 0:
                        cnt += 1
                        num = rows_map[i][k]
                if cnt == 1 and num > 1:
                    ok.appendleft(0*10**5 + i)
            c[i][j] = -1


ans = 0
for i in range(h):
    for j in range(w):
        if c[i][j] != -1:
            ans += 1

# print(*c, sep="\n")
print(ans)
