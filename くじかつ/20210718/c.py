h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]


ans = "Possible"
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            down = False
            right = False
            if i < h-1 and a[i+1][j] == "#":
                down = True
            if j < w-1 and a[i][j+1] == "#":
                right = True
            if not down ^ right and i != h-1 and j != w-1:
                ans = "Impossible"

            up = False
            left = False
            if 0 < i and a[i-1][j] == "#":
                up = True
            if 0 < j and a[i][j-1] == "#":
                left = True
            if not up ^ left and i != 0 and j != 0:
                ans = "Impossible"

print(ans)
