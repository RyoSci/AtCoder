a, b, k, l = map(int, input().split())
if a * l <= b:
    res = a * k
else:
    res = min(k // l * b + k % l * a, (k + l - 1) // l * b)

print(res)
