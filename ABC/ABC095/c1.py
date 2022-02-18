a, b, c, x, y = map(int, input().split())
res = min(a * x + b * y, c * 2 * x + max(0, y - x)
          * b, c * 2 * y + max(0, x - y) * a)
print(res)
