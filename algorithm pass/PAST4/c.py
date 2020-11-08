n, m = map(int, input().split())
s = [input() for i in range(n)]
ans = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        res = 0
        if i == 0 and i == n - 1:
            dx = [0]
        elif i == 0:
            dx = [0, 1]
        elif i == n - 1:
            dx = [-1, 0]
        else:
            dx = [-1, 0, 1]
        if j == 0 and j == m - 1:
            dy = [0]
        elif j == 0:
            dy = [0, 1]
        elif j == m - 1:
            dy = [-1, 0]
        else:
            dy = [-1, 0, 1]
        for ii in dx:
            for jj in dy:
                if s[i + ii][j + jj] == "#":
                    res += 1
        ans[i][j] = str(res)

for i in range(n):
    print("".join(ans[i]))
