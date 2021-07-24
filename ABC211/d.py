from collections import deque
n, m = map(int, input().split())

g = [[] for i in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)
    g[b].append(a)

mod = 10**9+7
dis = [-1]*n
cnt = [0]*n
dis[0] = 1
cnt[0] = 1
q = deque()
q.append([0, 1])

while len(q) != 0:
    pair, tmp_dis = q.popleft()
    for chi in g[pair]:
        if dis[chi] == -1:
            dis[chi] = tmp_dis
            cnt[chi] += cnt[pair]
            cnt[chi] %= mod
            q.append([chi, dis[chi]+1])
        elif dis[chi] == tmp_dis:
            cnt[chi] += cnt[pair]
            cnt[chi] %= mod

print(cnt[n-1])
