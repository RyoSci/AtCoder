import math
n = int(input())
a = list(map(int, input().split()))

gcd = a[0]
for i in range(1, n):
    gcd = math.gcd(a[i], gcd)
    if gcd == 1:
        print(1)
        break
else:
    print(gcd)