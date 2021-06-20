n = int(input())
g = [[] for _ in range(n)]

for i in range(n):
    u, _, *v = map(lambda x: int(x)-1, input().split())
    for vi in v:
        g[u].append(vi)

for i in range(n):
    g[i].sort()

passed = [[] for _ in range(n)]

cnt = 0


def dfs(pair):
    global cnt, passed
    cnt += 1
    passed[pair].append(cnt)
    for chi in g[pair]:
        if len(passed[chi]) == 0:
            dfs(chi)
    cnt += 1
    passed[pair].append(cnt)
    return


for i in range(n):
    if len(passed[i]) == 0:
        dfs(i)

for i, j in enumerate(passed):
    print(i+1, *j)
