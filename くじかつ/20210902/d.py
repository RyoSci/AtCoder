from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

q = deque()
q.append([0, 0, 1])
visit = [[0]*w for _ in range(h)]
visit[0][0] = 1


def bfs():
    while len(q) > 0:
        x, y, dis = q.popleft()
        if x == h-1 and y == w-1:
            return dis
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == "." and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append([nx, ny, dis+1])
    else:
        return -1


dis = bfs()
if dis == -1:
    print(-1)
else:
    res = h*w-dis
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                res -= 1
    print(res)
