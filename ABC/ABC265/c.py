# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
g = []
for i in range(h):
    s = input()
    tmp = []
    for j in s:
        if j == "U":
            tmp.append(0)
        elif j == "D":
            tmp.append(1)
        elif j == "L":
            tmp.append(2)
        else:
            tmp.append(3)

    g.append(tmp)


seen = [[0]*w for _ in range(h)]
x, y = 0, 0
seen[x][y] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
while 1:
    nx = x+dx[g[x][y]]
    ny = y+dy[g[x][y]]
    if 0 <= nx < h and 0 <= ny < w:
        if seen[nx][ny] == 1:
            ans = -1
            break
        seen[nx][ny] = 1
        x = nx
        y = ny
    else:
        break

if ans == -1:
    print(ans)
else:
    print(x+1, y+1)
