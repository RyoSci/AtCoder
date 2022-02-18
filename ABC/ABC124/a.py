a, b = map(int, input().split())

res = max(2*a - 1, a + b, 2*b - 1)

print(res)