from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, q = map(int, input().split())
x = list(map(int, input().split()))
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


dq_pre = deque()
INF = 10**18
dis = [INF]*n
dis[0] = 0
dq_pre.append(0)

dq = deque()
dp = [[] for _ in range(n)]

while len(dq_pre) > 0:
    par = dq_pre.popleft()
    for chi in g[par]:
        if dis[chi] < dis[par]:
            continue
        dis[chi] = dis[par]+1
        dq_pre.append(chi)

max_dis = max(dis)
same_dis = [[] for _ in range(max_dis+1)]

for i in range(n):
    same_dis[dis[i]].append(i)

for i in range(max_dis, -1, -1):
    for par in same_dis[i]:
        dp[par].append(x[par])
        dp[par].sort(reverse=True)
        dp[par] = dp[par][:20]
        for chi in g[par]:
            if dis[chi] > dis[par]:
                continue
            dp[chi] += dp[par]
            dp[chi].sort(reverse=True)
            dp[chi] = dp[chi][:20]

ans = []
for i in range(q):
    v, k = map(int, input().split())
    v -= 1
    k -= 1
    ans.append(dp[v][k])

print(*ans)
