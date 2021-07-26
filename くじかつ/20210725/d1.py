from collections import deque


n, m = map(int, input().split())
a = list(map(int, input().split()))

g = [[] for _ in range(n)]
for i in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    g[x].append(y)


def bfs(pair):
    global res
    q = deque()
    q.append(pair)
    while len(q) != 0:
        pair = q.popleft()
        res = max(res, a[pair]-cnt[pair])
        for chi in g[pair]:
            if p[chi] == 0:
                p[chi] = 1
                cnt[chi] = min(cnt[chi], cnt[pair])
                cnt[chi] = min(cnt[chi], a[pair])
                # res = max(res, a[chi]-cnt[chi])
                q.append(chi)
            else:
                cnt[chi] = min(cnt[chi], cnt[pair])
                cnt[chi] = min(cnt[chi], a[pair])
                # res = max(res, a[chi]-cnt[chi])


p = [0]*n
cnt = [10**18]*n
res = -10**18
for i in range(n):
    # if p[i] == 0:
    p[i] = 1
    bfs(i)

print(res)
