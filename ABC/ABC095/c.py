a, b, c, x, y = map(int, input().split())

res1 = a * x + b * y

if x < y:
    res2 = c * x * 2 + b * (y - x)
else:
    res2 = c * y * 2 + a * (x - y)

res3 = c * max(x, y) * 2

res = min(res1, res2, res3)
print(res)
