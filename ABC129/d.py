h, w = map(int, input().split())
s = [input() for _ in range(h)]
masu = [[0 for i in range(w)] for j in range(h)]

cnt = 0
tmp = []
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            cnt += 1
            tmp.append(j)
        if s[i][j] == "#" or s[i][j] == "." and j == w - 1:
            for k in tmp:
                masu[i][k] = cnt
            cnt = 0
            tmp = []

ans = 0
for j in range(w):
    for i in range(h):
        if s[i][j] == ".":
            cnt += 1
            tmp.append(i)
        if s[i][j] == "#" or s[i][j] == "." and i == h - 1:
            for k in tmp:
                masu[k][j] += cnt
                ans = max(ans, masu[k][j])
            cnt = 0
            tmp = []

print(ans - 1)
