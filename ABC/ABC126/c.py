import math
n , k = map(int, input().split())

res = 0
pi = 1 / n
for i in range(1, n + 1):
    i = k / i
    i = math.log2(i)
    if i <= 0:
        index = 0
    elif int(i) == i:
        index = int(i)
    else:
        index = int(i) + 1
    res += pi / (2 ** index)

print(res)
