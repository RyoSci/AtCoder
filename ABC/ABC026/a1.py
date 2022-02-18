a = int(input())
res = 0
for x in range(a + 1):
    y = a - x
    res = max(res, x * y)

print(res)
