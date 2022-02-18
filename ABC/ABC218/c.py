import numpy as np
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
s = [list(input().strip()) for _ in range(n)]
t = [list(input().strip()) for _ in range(n)]

min_si = 10**18
max_si = 0
min_sj = 10**18
max_sj = 0


for i in range(n):
    for j in range(n):
        if s[i][j] == "#":
            min_si = min(min_si, i)
            max_si = max(max_si, i)
            min_sj = min(min_sj, j)
            max_sj = max(max_sj, j)

a = max_si-min_si+1
b = max_sj-min_sj+1
sc = [["."]*b for _ in range(a)]

for i in range(n):
    for j in range(n):
        if s[i][j] == "#":
            sc[i-min_si][j-min_sj] = "#"

min_ti = 10**18
max_ti = 0
min_tj = 10**18
max_tj = 0

for i in range(n):
    for j in range(n):
        if t[i][j] == "#":
            min_ti = min(min_ti, i)
            max_ti = max(max_ti, i)
            min_tj = min(min_tj, j)
            max_tj = max(max_tj, j)

a = max_ti-min_ti+1
b = max_tj-min_tj+1
tc = [["."]*b for _ in range(a)]

for i in range(n):
    for j in range(n):
        if t[i][j] == "#":
            tc[i-min_ti][j-min_tj] = "#"

ans = "No"
sc = np.array(sc)
tc = np.array(tc)

for i in range(4):
    s_rot = np.rot90(sc, i)
    if s_rot.shape != tc.shape:
        continue
    if (s_rot == tc).all():
        ans = "Yes"

print(ans)
