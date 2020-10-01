import math
n = int(input())
r = sorted([int(input()) for i in range(n)], reverse=True)
s = 0
for i in range(n):
    if i % 2 == 0:
        s += r[i]**2
    else:
        s -= r[i]**2

print(s*math.pi)
