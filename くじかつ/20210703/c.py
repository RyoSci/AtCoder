from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

group = [-1]*n
d = deque()

for i in range(n):
    if group[i] != -1:
        continue
    d.append(i)
    group[i] = i
    while len(d) > 0:
        pair = d.popleft()
        for chi in g[pair]:
            if group[chi] != -1:
                continue
            group[chi] = i
            d.append(chi)

d = set(group)
res = len(list(d))

print(res-1)
