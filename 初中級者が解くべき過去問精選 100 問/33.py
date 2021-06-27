from collections import deque
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
queue = deque()
queue.append([0, 0])
dis = [[-1]*w for _ in range(h)]
dis[0][0] = 1

black = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            black += 1


def bfs():
    while len(queue) != 0:
        i, j = queue.popleft()
        cnt = dis[i][j]
        if i == h-1 and j == w-1:
            return cnt
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni = i+di
            nj = j+dj
            if 0 <= ni < h and 0 <= nj < w and dis[ni][nj] == -1:
                if s[ni][nj] == ".":
                    dis[ni][nj] = cnt+1
                    queue.append([ni, nj])
    return -1


res = bfs()
if res == -1:
    print(-1)
else:
    print(h*w-black-res)
