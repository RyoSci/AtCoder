import math
n = int(input())
a = list(map(int, input().split()))
lcm = a[0]
for i in range(1, n):
    lcm = lcm * a[i] // math.gcd(lcm, a[i])

res = 0
for i in range(n):
    res += (lcm - 1) % a[i]
print(res)