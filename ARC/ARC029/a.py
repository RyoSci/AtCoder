n = int(input())
t = [int(input()) for i in range(n)]

res = 100
for i in range(1 << n):
    a, b = 0, 0
    for j in range(n):
        if i >> j & 1:
            a += t[j]
        else:
            b += t[j]
    res = min(res, max(a, b))

print(res)