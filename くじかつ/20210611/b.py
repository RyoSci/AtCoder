h, w, x, y = map(int, input().split())
masu = [list(input()) for _ in range(h)]


def udlr(x, y, dir):
    res = 0
    while True:
        if not ((0 <= x < h and 0 <= y < w) and masu[x][y] != "#"):
            break
        res += 1
        if dir == 0:
            x -= 1
        elif dir == 1:
            x += 1
        elif dir == 2:
            y -= 1
        elif dir == 3:
            y += 1
    return res


x -= 1
y -= 1
res = 0
for i in range(4):
    res += udlr(x, y, i)
print(res-3)
