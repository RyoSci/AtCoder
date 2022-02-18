import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, x = map(int, input().split())
c = []
a = []
for i in range(n):
    ci, *ai = list(map(int, input().split()))
    c.append(ci)
    a.append(ai)

INF = 10**18
ans = INF
for i in range(1 << n):
    buy = [0]*n
    cost = 0
    for j in range(n):
        if i >> j & 1:
            buy[j] = 1
            cost += c[j]

    skills = [0]*m
    for j in range(n):
        if buy[j] == 0:
            continue
        for k in range(m):
            skills[k] += a[j][k]

    for j in range(m):
        if skills[j] < x:
            break
    else:
        ans = min(ans, cost)

if ans == INF:
    print(-1)
else:
    print(ans)
