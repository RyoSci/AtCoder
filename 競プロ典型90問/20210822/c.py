import sys
sys.setrecursionlimit(10**7)

h, w = map(int, input().split())
q = int(input())


def find(a):
    ax, ay = a
    if p[ax][ay] == [ax, ay]:
        return [ax, ay]
    p[ax][ay] = find(p[ax][ay])
    return p[ax][ay]


def unite(a, b):
    if find(a) == find(b):
        return
    ax, ay = find(a)
    bx, by = find(b)
    p[ax][ay] = p[bx][by]
    return


p = [[[i, j] for j in range(w)] for i in range(h)]
grid = [[0]*w for _ in range(h)]
ans = []
for i in range(q):
    qi = list(map(lambda x: int(x)-1, input().split()))
    if len(qi) == 3:
        _, ra, ca = qi
        grid[ra][ca] = 1
        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nx = ra+dx
            ny = ca+dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 1:
                unite([ra, ca], [nx, ny])
    else:
        _, ra, ca, rb, cb = qi
        if find([ra, ca]) == find([rb, cb]) and grid[ra][ca]*grid[rb][cb] == 1:
            ans.append("Yes")
        else:
            ans.append("No")

print(*ans, sep="\n")
