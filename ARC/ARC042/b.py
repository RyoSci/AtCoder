x, y = map(int, input().split())
n = int(input())
res = 101
vertics = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    i = (i + 1) % n - 1
    a = -vertics[i][1] + vertics[i + 1][1]
    b = vertics[i][0] - vertics[i + 1][0]
    c = -vertics[i][1] * (vertics[i][0] - vertics[i + 1][0]) + \
        vertics[i][0] * (vertics[i][1] - vertics[i + 1][1])
    l = abs(a * x + b * y + c) / ((a ** 2 + b ** 2) ** 0.5)
    res = min(res, l)

print(res)
