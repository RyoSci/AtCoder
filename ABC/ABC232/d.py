from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

h, w = map(int, input().split())
c = [list(input().strip()) for _ in range(h)]

seen = [[0]*w for _ in range(h)]


q = deque()
q.append((0, 0))
seen[0][0] = 1

while len(q) > 0:
    x, y = q.popleft()
    for dx, dy in [[0, 1], [1, 0]]:
        nx = x+dx
        ny = y+dy
        if nx < h and ny < w and c[nx][ny] != '#' and seen[nx][ny] != 1:
            seen[nx][ny] = 1
            q.append((nx, ny))

ans = 0
for i in range(h):
    for j in range(w):
        if seen[i][j] == 1:
            ans = max(ans, i+j+1)

print(ans)
