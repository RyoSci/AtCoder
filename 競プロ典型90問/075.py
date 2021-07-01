import math
n = int(input())
d = dict()
n_ = n
for i in range(2, n_+1):
    while 1:
        if n % i == 0:
            if i not in d:
                d[i] = 0
            d[i] += 1
            n //= i
        else:
            break
    if n == 1:
        break
    if i**2 > n:
        d[n] = 1
        break

num = sum(d.values())

print(math.ceil(math.log2(num)))
