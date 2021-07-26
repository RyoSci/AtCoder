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

    def dfs(pair):
        global res
        res = max(res, a[pair]-cnt[pair])
        for chi in g[pair]:
            if p[chi] == 0:
                p[chi] = 1
                # res = max(res, a[chi]-cnt[chi])
                cnt[chi] = min(cnt[chi], cnt[pair])
                cnt[chi] = min(cnt[chi], a[pair])
                dfs(chi)
            else:
                # res = max(res, a[chi]-cnt[chi])
                cnt[chi] = min(cnt[chi], cnt[pair])
                cnt[chi] = min(cnt[chi], a[pair])


p = [0]*n
cnt = [10**18]*n
res = -10**18
for i in range(n):
    # if p[i] == 0:
    p[i] = 1
    dfs(i)

print(res)
