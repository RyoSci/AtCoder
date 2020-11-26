k, a, b = map(int, input().split())

res = 0
if 2 < b - a:
    if k >= a:
        res = b + (k - a - 1) // 2 * (b - a) + (k - a - 1) % 2
    else:
        res = k + 1
else:
    res = k + 1

print(max(res, k + 1))
