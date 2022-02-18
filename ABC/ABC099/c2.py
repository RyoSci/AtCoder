import math
n = int(input())
print(math.log(10 ** 5, 9))
print(math.log(10 ** 5, 6))
res = 10 ** 5
for nine in range(6, -1, -1):
    for six in range(7, -1, -1):
        tmp = n - 9 ** nine - 6 ** six + 2
        print(tmp)
        if tmp > 0:
            res = min(res, tmp)

print(res)
