a, b = map(int, input().split())
res = max(a + b, a - b, a * b)
print(res)
