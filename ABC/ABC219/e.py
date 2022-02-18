import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


a = [list(map(int, input().split())) for _ in range(4)]

n = 0
for i in range(4):
    for j in range(4):
        if a[i][j] == 1:
            n += 1


res = 0
for i in range(1 << 16):
    flags = [0]*16
    for j in range(16):
        if i >> j & 1:
            flags[j] = 1
    cnt = 0
    for j in range(16):
        ok = False
        if flags[j] == 1:
            x, y = j//4, j % 4
            cnt += 1
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nx = x+dx
                ny = y+dy
                if 0 <= nx < 4 and 0 <= ny < 4:
                    jj = nx*4+ny
                    if flags[jj] == 1:
                        ok = True
                        break

        if not ok:
            break
    if ok and cnt == n:
        res += 1

print(res)
