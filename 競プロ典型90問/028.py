n = int(input())
imos = [[0 for j in range(1001)] for i in range(1001)]

for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    imos[lx][ly] += 1
    imos[rx][ly] -= 1
    imos[lx][ry] -= 1
    imos[rx][ry] += 1

for i in range(1001):
    for j in range(1, 1001):
        imos[i][j] += imos[i][j-1]

for j in range(1001):
    for i in range(1, 1001):
        imos[i][j] += imos[i-1][j]

ans = [0]*(n+1)
for i in range(1001):
    for j in range(1001):
        ans[imos[i][j]] += 1

for i in range(1, n+1):
    print(ans[i])
