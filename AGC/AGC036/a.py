import math
s = int(input())
# s = 9 * 10 ** 17 + 9 * 10 ** 8 + 5
s_div = s // (10 ** 9)
s_mod = s % (10 ** 9)
x1, y1 = 0, 0
x2, y3 = 10 ** 9, s_div + (s_mod > 0)
x3, y2 = 1, (10 ** 9) * (s_mod > 0) - s_mod
print(x1, y1, x2, y2, x3, y3)
# print(x2 * y3 - x3 * y2 == s)
