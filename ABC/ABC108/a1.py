k = int(input())
if k % 2 == 0:
    res = (k // 2) ** 2
else:
    res = (k // 2) * (k // 2 + 1)

print(res)