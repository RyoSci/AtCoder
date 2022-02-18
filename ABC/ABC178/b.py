a, b, c, d = map(int, input().split())
res = max(a * c, b * d, a * d, b * c)
print(res)
