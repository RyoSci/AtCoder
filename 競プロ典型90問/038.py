a, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a*b//gcd(a, b)


res = "Large" if lcm(a, b) > 10**18 else lcm(a, b)
print(res)
