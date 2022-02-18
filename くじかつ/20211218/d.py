import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

h, w = map(int, input().split())
s = [input().strip() for _ in range(h)]

dpx = [[0]*w for _ in range(h)]
dpy = [[0]*w for _ in range(h)]

for j in range(w):
    for i in range(h):
        if s[i][j] == '#':
            continue
        if dpx[i][j] != 0:
            continue
        ni = i
        tmp = 0
        while 1:
            if ni < h and s[ni][j] == '.':
                tmp += 1
                ni += 1
            else:
                break
        for ii in range(i, ni):
            dpx[ii][j] = tmp

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue
        if dpy[i][j] != 0:
            continue
        nj = j
        tmp = 0
        while 1:
            if nj < w and s[i][nj] == '.':
                tmp += 1
                nj += 1
            else:
                break
        for jj in range(j, nj):
            dpy[i][jj] = tmp

ans = 1

for i in range(h):
    for j in range(w):
        ans = max(ans, dpx[i][j]+dpy[i][j]-1)

print(ans)

# print(*dpx, sep="\n")
# print(*dpy, sep="\n")
