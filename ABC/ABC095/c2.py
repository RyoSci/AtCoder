a, b, c, x, y = map(int, input().split())
n = max(x, y) * 2
res = 10 ** 9 + 10
for i in range(0, n + 1, 2):
    tmp = c * i + a * max(x - i // 2, 0) + b * max(y - i // 2, 0)
    res = min(tmp, res)
print(res)
