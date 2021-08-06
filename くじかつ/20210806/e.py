h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

p = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        p[i][j] = [i, j]


def find(x):
    xi, xj = x
    if p[xi][xj] == [xi, xj]:
        return [xi, xj]
    p[xi][xj] = find(p[xi][xj])
    return p[xi][xj]


def unite(x, y):
    xi, xj = x
    yi, yj = y
    if find(x) == find(y):
        return
    p[xi][xj] = find(p[yi][yj])


for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            for ii, jj in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
                if 0 <= i+ii < h and 0 <= j+jj < w and s[i+ii][j+jj] == "#" and (s[i][j+jj] == "." or s[i+ii][j] == "."):
                    unite([i, j], [i+ii, j+jj])

d = dict()
for i in range(h):
    for j in range(w):
        p[i][j] = find(p[i][j])
        if s[i][j] == "#":
            if (p[i][j][0], p[i][j][1]) not in d:
                d[(p[i][j][0], p[i][j][1])] = []
            d[(p[i][j][0], p[i][j][1])].append((i, j))

res = 0
for key, vals in d.items():
    tmp = set()
    for val in vals:
        for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            if 0 <= val[0]+i < h and 0 <= val[1]+j < w and s[val[0]+i][val[1]+j] == ".":
                tmp.add((val[0]+i, val[1]+j))
    res += len(vals)*len(tmp)

print(res)
print(d)
