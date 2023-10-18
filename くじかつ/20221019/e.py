# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = []
for i in range(n):
    ai = list(map(int, input().split()))
    a.append(ai)

p = [[0]*n for _ in range(n)]
g = [[[] for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n-2):
        pre = [i, a[i][j]-1]
        pre.sort()

        nxt = [i, a[i][j+1]-1]
        nxt.sort()

        g[pre[0]][pre[1]].append(nxt)
        p[nxt[0]][nxt[1]] += 1


q = deque()

cnt = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if p[i][j] == 0:
            q.append((i, j))
            cnt[i][j] = 1


while len(q) > 0:
    # i, j = q.pop()
    i, j = q.popleft()
    for ni, nj in g[i][j]:
        p[ni][nj] -= 1
        if p[ni][nj] == 0:
            cnt[ni][nj] = cnt[i][j]+1
            q.append((ni, nj))
        # print(f"{cnt[i][j]=}, {cnt[ni][nj]=}, {ni=}, {nj=}, {i=}, {j=}")
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, cnt[i][j])
        if p[i][j] > 0:
            print(-1)
            exit()

print(ans)
# print(p)
# print(g)
# for i in range(n):
#     print(*cnt[i])
