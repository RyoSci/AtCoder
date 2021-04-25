h, w = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(h)]

# h, w = 2000, 2000
# a = [[j for j in range(w)] for i in range(h)]

col = [0] * h
for i in range(h):
    tmp = 0
    for j in a[i]:
        tmp += j
    col[i] = tmp

row = [0] * w
for i in range(w):
    tmp = 0
    for j in range(h):
        tmp += a[j][i]
    row[i] = tmp

for i in range(h):
    line = []
    for j in range(w):
        line.append(col[i] + row[j] - a[i][j])
    print(*line)
