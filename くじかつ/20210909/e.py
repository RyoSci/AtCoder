from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

h, w = map(int, input().split())
# h, w = 500, 500
# s = [list("#"*500) for _ in range(500)]
s = [list(input().strip()) for _ in range(h)]

dq = deque()
dq.append([0, 0, 0])
visit = [[10**18]*w for _ in range(h)]
visit[0][0] = 0

res = 10**18
while len(dq) > 0:
    x, y, cnt = dq.popleft()
    if x == h-1 and y == w-1:
        break
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nx = x+dx
        ny = y+dy
        if 0 <= nx < h and 0 <= ny < w:
            if visit[nx][ny] <= cnt:
                continue
            if s[nx][ny] == ".":
                visit[nx][ny] = cnt
                dq.appendleft([nx, ny, cnt])
            else:
                if visit[nx][ny] <= cnt+1:
                    continue
                visit[nx][ny] = cnt+1
                dq.append([nx, ny, cnt+1])

    for dx in [-1, 0, 1]:
        for dy in [-2, -1, 1, 2]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < h and 0 <= ny < w:
                if visit[nx][ny] <= cnt+1:
                    continue
                visit[nx][ny] = cnt+1
                dq.append([nx, ny, cnt+1])

    for dx in [-2, -1, 1, 2]:
        for dy in [-1, 0, 1]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < h and 0 <= ny < w:
                if visit[nx][ny] <= cnt+1:
                    continue
                visit[nx][ny] = cnt+1
                dq.append([nx, ny, cnt+1])


print(visit[h-1][w-1])
