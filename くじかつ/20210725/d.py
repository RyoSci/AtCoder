from sys import setrecursionlimit
setrecursionlimit(10**6)

n, m = map(int, input().split())
a = list(map(int, input().split()))

g = [[] for _ in range(n)]
for i in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    g[x].append(y)

for i in range(n):
    g[i].sort()


def dfs(pair, tmp_cnt):
    global res
    for chi in g[pair]:
        if p[chi] == 0:
            p[chi] = 1
            cnt[chi] = min(cnt[chi], tmp_cnt)
            res = max(res, a[chi]-cnt[chi])
            dfs(chi, min(cnt[pair], a[chi]))
        else:
            cnt[chi] = min(cnt[chi], tmp_cnt)
            res = max(res, a[chi]-cnt[chi])


p = [0]*n
cnt = [10**18]*n
res = -10**18
for i in range(n):
    if p[i] == 0:
        p[i] = 1
        dfs(i, a[i])

print(res)
