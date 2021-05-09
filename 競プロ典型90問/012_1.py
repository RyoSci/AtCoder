h, w = map(int, input().split())
q = int(input())
masu = [[[i, j] for j in range(w)] for i in range(h)]
red = [[0 for j in range(w)] for i in range(h)]


def find(xy):
    x, y = xy
    if masu[x][y] == [x, y]:
        return [x, y]

    masu[x][y] = find(masu[x][y])
    return masu[x][y]


def union(a, b, c, d):
    if find([a, b]) == find([c, d]):
        return
    masu[find([a, b])[0]][find([a, b])[1]
                          ] = masu[find([c, d])[0]][find([c, d])[1]]


for i in range(q):
    qi = list(map(int, input().split()))
    if qi[0] == 1:
        _, x, y = map(lambda x: x-1, qi)
        # masu[x][y] = [x, y]
        red[x][y] = 1
        for dx, dy in ([-1, 0], [0, 1], [1, 0], [0, -1]):
            xx = x+dx
            yy = y+dy
            if 0 <= xx < h and 0 <= yy < w:
                if red[x][y] == red[xx][yy] == 1:
                    union(x, y, xx, yy)
    else:
        _, a, b, c, d = map(lambda x: x-1, qi)
        if a == c and b == d:
            if red[a][b] == 1:
                print("Yes")
            else:
                print("No")
        elif find([a, b]) == find([c, d]):
            print("Yes")
        else:
            print("No")
