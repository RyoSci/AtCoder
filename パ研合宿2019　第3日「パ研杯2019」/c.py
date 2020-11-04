n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

res = 0
for i in range(m - 1):
    for j in range(i + 1, m):
        tmp = 0
        for k in range(n):
            tmp += max(a[k][i], a[k][j])
        res = max(res, tmp)

print(res)
