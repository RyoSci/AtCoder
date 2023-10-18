# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

s = []

for _ in range(n):
    si = input()
    s.append(list(si))

dis = [[INF]*n for _ in range(n)]
cost = [[0]*n for _ in range(n)]
for i in range(n):
    dis[i][i] = 0
    cost[i][i] = a[i]
    for j in range(n):
        if s[i][j] == "Y":
            dis[i][j] = 1
            cost[i][j] = max(cost[i][j], a[i]+a[j])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dis[i][j] > dis[i][k]+dis[k][j]:
                dis[i][j] = dis[i][k]+dis[k][j]
                cost[i][j] = cost[i][k] + cost[k][j] - a[k]
            elif dis[i][j] == dis[i][k]+dis[k][j]:
                if cost[i][j] < cost[i][k] + cost[k][j] - a[k]:
                    cost[i][j] = cost[i][k] + cost[k][j] - a[k]

q = int(input())
ans = []
for i in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    if dis[u][v] == INF:
        print("Impossible")
    else:
        print(dis[u][v], cost[u][v])
