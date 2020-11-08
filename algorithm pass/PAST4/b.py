import math
x, y = map(int, input().split())
if y == 0:
    print("ERROR")
else:
    n = 2
    res = math.floor(x / y * 10 ** n) / (10 ** n)
    print('{:.2f}'.format(res))
