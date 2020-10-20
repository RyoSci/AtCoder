import math
a, b, x = map(int, input().split())
pi = math.pi
harf = a * a * b / 2
if a * a * b == x:
    res = 0
elif x <= harf:
    res = math.degrees(math.atan(a * b * b / (2 * x)))

else:
    res = math.degrees(math.atan(a ** 3 / (2 * a * a * b - 2 * x)))
    res = 90 - res

print(res)
