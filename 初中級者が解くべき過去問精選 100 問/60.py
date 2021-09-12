v, e = map(int, input().split())
INF = 10**18
dp = [[INF]*v for _ in range(v)]

for i in range(v):
    dp[i][i] = 0


# g = [[] for _ in range(v)]
g = [[INF]]
for i in range(e):
    s, t, d = map(int, input().split())
    dp[s][t] = d
    # g[s].append([t, d])


for k in range(v):
    for i in range(v):
        for j in range(v):
            if dp[k][j] == INF or dp[i][k] == INF:
                continue
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

flag = False

for k in range(v):
    for i in range(v):
        for j in range(v):
            if dp[k][j] == INF or dp[i][k] == INF:
                continue
            if dp[i][j] > dp[i][k]+dp[k][j]:
                flag = True
                break

if flag:
    print("NEGATIVE CYCLE")
    exit()

for i in range(v):
    line = []
    for j in range(v):
        if dp[i][j] == INF:
            line.append("INF")
        else:
            line.append(dp[i][j])
    print(*line)
