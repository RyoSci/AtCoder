r, c, d = map(int, input().split())
a = [input().split() for _ in range(r)]

res = 0
for i in range(r):
    for j in range(c):
        if not ((i + j) % 2 ^ (d % 2)) and i + j <= d:
            res = max(res, int(a[i][j]))

print(res)