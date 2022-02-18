n, a, b = map(int, input().split())
res = max(0, (n - 2) * b - (n - 2) * a + 1)
print(res)
