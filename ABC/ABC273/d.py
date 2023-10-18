# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_right
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


h, w, rs, cs = map(int, input().split())
rs -= 1
cs -= 1
n = int(input())
col = dict()
row = dict()
for i in range(n):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    if r not in row:
        row[r] = [-1, w]
    row[r].append(c)
    if c not in col:
        col[c] = [-1, h]
    col[c].append(r)

# print(row)
# print(col)

for key in row.keys():
    row[key].sort()

for key in col.keys():
    col[key].sort()

ans = []
q = int(input())
for i in range(q):
    d, l = list(map(str, input().split()))
    l = int(l)
    if d == "L":
        if rs in row:
            pos = bisect_right(row[rs], cs)
            cs = max(row[rs][pos-1]+1, cs-l)
        else:
            cs = max(0, cs-l)

    if d == "R":
        if rs in row:
            pos = bisect_right(row[rs], cs)
            cs = min(row[rs][pos]-1, cs+l)
        else:
            cs = min(w-1, cs+l)

    if d == "U":
        if cs in col:
            pos = bisect_right(col[cs], rs)
            rs = max(col[cs][pos-1]+1, rs-l)
        else:
            rs = max(0, rs-l)

    if d == "D":
        if cs in col:
            pos = bisect_right(col[cs], rs)
            rs = min(col[cs][pos]-1, rs+l)
        else:
            rs = min(h-1, rs+l)

    ans.append((rs+1, cs+1))

for i in range(q):
    print(*ans[i])
