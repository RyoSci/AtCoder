n = int(input())
a = list(map(int, input().split()))
res = 100
for i in range(n):
    for j in range(100):
        if a[i] % 2 == 1:
            break
        a[i] //= 2
    res = min(res, j)
    if res == 0:
        break
print(res)
