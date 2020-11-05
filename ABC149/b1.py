a, b, k = map(int, input().split())

minus_a = min(a, k)
a -= minus_a
b = max(b - (k - minus_a), 0)

print(a, b)
