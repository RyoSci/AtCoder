# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
ax, ay = map(lambda x: int(x)-1, input().split())
bx, by = map(lambda x: int(x)-1, input().split())

s = [list(input()) for _ in range(n)]

dis = [[INF]*(n) for _ in range(n)]
dis[ax][ay] = 0


q = deque()
x = ax
y = ay
q.append((x, y))


def process(x, y):
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]
    for i in range(4):
        nx = x
        ny = y
        while 1:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < n and s[nx][ny] == "." and dis[nx][ny] == INF:
                dis[nx][ny] = dis[x][y]+1
                q.append((nx, ny))
            elif 0 <= nx < n and 0 <= ny < n and s[nx][ny] == "." and dis[nx][ny] == dis[x][y]+1:
                continue
            else:
                break


while len(q):
    x, y = q.popleft()
    process(x, y)

if dis[bx][by] == INF:
    print(-1)
else:
    print(dis[bx][by])
