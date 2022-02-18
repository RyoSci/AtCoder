from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


a, n = map(int, input().split())
q = deque()
INF = 10**18
m = 10**6
dis = [INF]*(m)
dis[1] = 0
q.append(1)

while len(q) > 0:
    now = q.popleft()
    next = now*a
    if next <= m and dis[next] > dis[now]+1:
        dis[next] = dis[now]+1
        q.append(next)
    if now < 10 or now % 10 == 0:
        continue
    else:
        next = str(now)
        for i in range(len(next)):
            if next[-1] == '0':
                break
            next = next[-1]+next[:-1]
            if int(next) <= m and dis[int(next)] > dis[now]+i+1:
                dis[int(next)] = dis[now]+i+1
                q.append(int(next))

if dis[n] == INF:
    print(-1)
else:
    print(dis[n])
