from collections import deque
n = int(input())
g = [[] for _ in range(n)]

for i in range(n):
    u, k, *v = map(int, input().split())
    for vi in v:
        g[u-1].append(vi-1)

dis = [-1]*n
dis[0] = 0

d = deque()
d.append((0, 0))

while len(d) != 0:
    pair, cnt = d.popleft()
    for chi in g[pair]:
        if dis[chi] == -1:
            d.append((chi, cnt+1))
            dis[chi] = cnt+1

for i in range(n):
    print(i+1, dis[i])
