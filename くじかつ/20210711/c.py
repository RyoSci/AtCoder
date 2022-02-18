n = int(input())


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def lcm(x, y):
    return x*y//gcd(x, y)


res = 1
for i in range(n):
    t = int(input())
    res = lcm(res, t)

print(res)
