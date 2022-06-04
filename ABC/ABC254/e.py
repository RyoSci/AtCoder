# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())


G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dp = [[0]*5 for _ in range(n)]
for i in range(n):
    dp[i][0] = i+1


def bfs(par):
    q = deque()
    now = 1
    q.append([par, -1, now])
    res = set()
    res.add(par+1)
    while len(q) > 0:
        to, root, now = q.popleft()
        if now == 4:
            break
        for chi in G[to]:
            if chi == root:
                continue
            if chi+1 not in res:
                q.append([chi, to, now+1])
                res.add(chi+1)
        dp[par][now] = sum(res)


for i in range(n):
    bfs(i)

for i in range(n):
    for j in range(1, 4):
        dp[i][j] = max(dp[i][j], dp[i][j-1])
ans = []
Q = int(input())
for i in range(Q):
    x, k = map(int, input().split())
    ans.append(dp[x-1][k])

print(*ans)
# print(dp)
