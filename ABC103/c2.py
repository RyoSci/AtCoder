import typing
n = int(input())
a = list(map(int, input().split()))

def gcd(x : int, y : int):
    x, y = min(x, y), max(x, y)
    while True:
        mod = y % x
        if mod == 0:
            break
        y = x
        x = mod

    return x

lcm = a[0]
for i in range(1, n):
    lcm = lcm * a[i] // gcd(lcm, a[i])

res = 0
for i in range(n):
    res += (lcm - 1) % a[i]
print(res)