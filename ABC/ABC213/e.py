from collections import deque

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

dis = [[10**6]*w for _ in range(h)]
dis[0][0] = 0

wall = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
for i in range(-1, 2, 1):
    wall.append([i, -2])
    wall.append([i, 2])
    wall.append([-2, i])
    wall.append([2, i])

dq = deque()
cnt = 0
dq.append([0, 0, cnt])
while len(dq) != 0:
    x, y, cnt = dq.pop()
    if x == h-1 and y == w-1:
        break
    for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        xx = x+dx
        yy = y+dy
        if 0 <= xx < h and 0 <= yy < w and dis[xx][yy] > cnt and s[xx][yy] == ".":
            dis[xx][yy] = cnt
            dq.append([xx, yy, cnt])
        if 0 <= xx < h and 0 <= yy < w and dis[xx][yy] > cnt+1 and s[xx][yy] == "#":
            dis[xx][yy] = cnt+1
            dq.appendleft([xx, yy, cnt+1])
    for dx, dy in wall:
        xx = x+dx
        yy = y+dy
        if 0 <= xx < h and 0 <= yy < w and dis[xx][yy] > cnt+1:
            dis[xx][yy] = cnt+1
            dq.appendleft([xx, yy, cnt+1])

print(dis[h-1][w-1])
