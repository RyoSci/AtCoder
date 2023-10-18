# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n, m = map(int, input().split())

d = dict()
for i in range(0, 2*n):
    d[i*i] = [i, -i]

cnt = [[INF]*n for _ in range(n)]
q = deque()
q.append([1, 1])
cnt[0][0] = 0

while len(q) > 0:
    px, py = q.popleft()
    for nx in range(1, n+1):
        ny2 = m - (nx-px)**2
        if ny2 in d:
            for i in d[ny2]:
                ny = i+py
                if 1 <= ny <= n and cnt[nx-1][ny-1] > cnt[px-1][py-1]+1:
                    cnt[nx-1][ny-1] = cnt[px-1][py-1]+1
                    q.append([nx, ny])
        # print(px, py, nx, ny2)


for i in range(n):
    for j in range(n):
        if cnt[i][j] >= INF:
            cnt[i][j] = -1
    print(*cnt[i])
