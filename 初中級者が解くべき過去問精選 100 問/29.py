from collections import deque
r, c = map(int, input().split())
sy, sx = map(lambda x: int(x)-1, input().split())
gy, gx = map(lambda x: int(x)-1, input().split())
grid = [list(input()) for _ in range(r)]

q = deque()
q.append((sy, sx))
dis = [[-1 for j in range(c)] for i in range(r)]
dis[sy][sx] = 0
res = 0

while len(q) != 0:
    y, x = q.popleft()
    tmp = dis[y][x]
    for dy, dx in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        if y+dy == gy and x+dx == gx:
            res = tmp+1
            print(res)
            exit()
        elif grid[y+dy][x+dx] == "." and dis[y+dy][x+dx] == -1:
            dis[y+dy][x+dx] = tmp+1
            q.append((y+dy, x+dx))
