from collections import deque
h, w, n = map(int, input().split())
grid = [list(input()) for _ in range(h)]
pos = [[] for _ in range(n+1)]
for i in range(h):
    for j in range(w):
        if grid[i][j] != "." and grid[i][j] != "X":
            if grid[i][j] == "S":
                pos[0] = [i, j]
            else:
                pos[int(grid[i][j])] = [i, j]


def bfs(s, g):
    sx, sy = pos[s]
    gx, gy = pos[g]
    dis = [[-1 for j in range(w)] for i in range(h)]
    dis[sx][sy] = 0
    queue = deque()
    queue.append([sx, sy])
    while len(queue) != 0:
        x, y = queue.popleft()
        tmp = dis[x][y]
        if x == gx and y == gy:
            return tmp
        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != "X":
                if dis[nx][ny] == -1:
                    dis[nx][ny] = tmp+1
                    queue.append([nx, ny])


res = 0
for i in range(n):
    res += bfs(i, i+1)

print(res)
