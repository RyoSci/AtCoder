n = int(input())
res = 10 ** 5
for i in range(1, int(n ** 0.5) + 1):
    res = min(res, abs(i - n // i) + n - i * (n // i))

print(res)
