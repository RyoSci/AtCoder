from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[]*n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


q = deque()
q.append(0)
INF = 10**18
dis = [INF]*n
dis[0] = 0
p = [-1]*n

while len(q) > 0:
    x = q.popleft()
    for chi in g[x]:
        if dis[chi] <= dis[x]+1:
            continue
        dis[chi] = dis[x]+1
        p[chi] = x+1
        q.append(chi)

if INF in dis:
    print("No")
else:
    print("Yes")
    print(*p[1:], sep="\n")
