n = int(input())
res = 10 ** 5
for i in range(1, n + 1):
    res = min(res, abs(i - n // i) + n - i * (n // i))

print(res)
