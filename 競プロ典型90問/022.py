a, b, c = map(int, input().split())


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


egde = gcd(gcd(a, b), c)
res = a // egde + b // egde + c // egde - 3
print(res)
