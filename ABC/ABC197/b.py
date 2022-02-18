h, w, x, y = map(int, input().split())
s = [list(input()) for _ in range(h)]

x -= 1
y -= 1

ans = 0
if s[x][y] == ".":
    ans += 1

    for i_, j_ in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        cnt = 1
        while True:
            i = i_ * cnt
            j = j_ * cnt
            if 0 <= x + i < h and 0 <= y + j < w:
                if s[x + i][y + j] == ".":
                    ans += 1
                else:
                    break
            else:
                break
            cnt += 1

print(ans)
