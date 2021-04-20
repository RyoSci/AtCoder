n, m = map(int, input().split())
b = [list(map(int, list(input()))) for _ in range(n)]
a = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if b[i][j] > 0:
            tmp = b[i][j]
            for di, dj in [[0, 0], [1, -1], [1, 1], [2, 0]]:
                b[i + di][j + dj] -= tmp
            a[i + 1][j] += tmp


for i in range(n):
    print("".join(map(str, a[i])))
