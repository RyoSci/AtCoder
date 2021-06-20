import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    for ii in range(-1, 2, 1):
        for jj in range(-1, 2, 1):
            if 0 <= i+ii < h and 0 <= j+jj < w:
                if passed[i+ii][j+jj] == 0 and sea[i+ii][j+jj] == 1:
                    passed[i+ii][j+jj] = 1
                    dfs(i+ii, j+jj)
    return


wh = []
seas = []

while 1:
    w, h = map(int, input().split())
    wh.append([w, h])
    if w == 0 and h == 0:
        break
    sea = [list(map(int, input().split())) for _ in range(h)]
    seas.append(sea)

for (w, h), sea in zip(wh, seas):
    passed = [[0 for j in range(w)] for i in range(h)]
    res = 0
    for i in range(h):
        for j in range(w):
            if sea[i][j] == 1 and passed[i][j] == 0:
                passed[i][j] = 1
                dfs(i, j)
                res += 1
    print(res)
