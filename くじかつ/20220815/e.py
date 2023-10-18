# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = []

for i in range(n):
    ai = list(map(lambda x: int(x)-1, input().split()))
    a.append(ai)


p = [[0]*n for _ in range(n)]
g = [[[] for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(1, n-1):
        x = i
        y = a[i][j]
        if x > y:
            x, y = y, x
        p[x][y] += 1

    for j in range(n-2):
        x = i
        y = a[i][j]
        if x > y:
            x, y = y, x

        tmp = [i, a[i][j+1]]
        tmp.sort()
        g[x][y].append(tmp)

q = deque()
for i in range(n-1):
    for j in range(i+1, n):
        if p[i][j] == 0:
            q.append((i, j, 1))

ans = 0
while len(q) > 0:
    i, j, cnt = q.popleft()
    ans = cnt
    for ni, nj in g[i][j]:
        p[ni][nj] -= 1
        if p[ni][nj] == 0:
            q.append((ni, nj, cnt+1))

flag = True
for i in range(n-1):
    for j in range(i+1, n):
        if p[i][j] > 0:
            flag = False
if flag:
    print(ans)
else:
    print(-1)
