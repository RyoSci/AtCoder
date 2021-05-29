h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
mod = 998244353
ans = 1
blank = 0
for i in range(h):
    has_red = False
    has_blue = False

    x = h - 1 - i
    y = 0

    while 0 <= x < h and 0 <= y < w:
        if s[x][y] == "R":
            has_red = True
        elif s[x][y] == "B":
            has_blue = True
        x -= 1
        y += 1

    if has_red and has_blue:
        ans = 0
        break
    elif not(has_red or has_blue):
        blank += 1


for j in range(1, w):
    has_red = False
    has_blue = False

    x = h-1
    y = j

    while 0 <= x < h and 0 <= y < w:
        if s[x][y] == "R":
            has_red = True
        elif s[x][y] == "B":
            has_blue = True
        x -= 1
        y += 1

    if has_red and has_blue:
        ans = 0
        break
    elif not(has_red or has_blue):
        blank += 1


if ans == 0:
    print(ans)
else:
    for i in range(blank):
        ans = ans * 2 % mod
    print(ans)
