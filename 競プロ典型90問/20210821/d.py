import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

g1 = [[] for _ in range(n)]
g2 = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g1[a].append(b)
    g2[b].append(a)


def dfs1(pair, cnt):
    for chi in g1[pair]:
        if visit[chi] == 0:
            visit[chi] = 1
            cnt = dfs1(chi, cnt)
    p[pair].append(cnt)
    return cnt+1


p = [[i] for i in range(n)]
visit = [0]*n
cnt = 1
for i in range(n):
    if visit[i] == 0:
        visit[i] = 1
        cnt = dfs1(i, cnt)

p.sort(key=lambda x: x[1], reverse=True)


def dfs2(pair, cnt):
    for chi in g2[pair]:
        if visit[chi] == 0:
            visit[chi] = 1
            cnt = dfs2(chi, cnt)
    return cnt+1


visit = [0]*n
res = 0
for i in range(n):
    i = p[i][0]
    if visit[i] == 0:
        visit[i] = 1
        cnt = dfs2(i, 0)
        res += cnt*(cnt-1)//2


print(res)
