n, a, b = map(int, input().split())
res = 0
for i in range(1, n + 1):
    i = str(i)
    keta = 0
    for j in i:
        keta += int(j)
    if a <= keta <= b:
        res += int(i)

print(res)
