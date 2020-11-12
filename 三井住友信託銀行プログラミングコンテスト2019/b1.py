import math
n = int(input())

l = math.ceil(n / 1.08)
r = math.ceil((n + 1) / 1.08) - 1


if l == r:
    print(l)

else:
    print(":(")
