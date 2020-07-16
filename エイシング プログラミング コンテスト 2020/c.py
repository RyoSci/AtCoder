n = int(input())
a = [0] * (n + 1)

for x in range(1, 10**2 + 1):
    for y in range(1, 10**2 + 1):
        for z in range(1, 10**2 + 1):
            tmp = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if tmp <= n:
                a[tmp] += 1
for i in range(1, n + 1):
    print(a[i])