import math
a, b, c = map(int, input().split())
max_r = a + b + c

if sorted([a, b, c])[-1] <= a + b + c - sorted([a, b, c])[-1]:
    min_r = 0
else:
    min_r = min(abs(a - b - c), abs(b - a - c), abs(c - a - b))
print(math.pi * (max_r ** 2 - min_r ** 2))
