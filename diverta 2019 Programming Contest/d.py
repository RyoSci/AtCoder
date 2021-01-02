from math import ceil
n = int(input())
b = (-1 + (1 + 4 * n) ** 0.5) / 2

m = 0
for i in range(1, ceil(b)):
    if (n - i) % i == 0:
        m += (n - i) // i

print(m)
