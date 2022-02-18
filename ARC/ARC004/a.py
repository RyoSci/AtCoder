n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        tmp = (xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2
        res = max(res, tmp ** 0.5)

print(res)
