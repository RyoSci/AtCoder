a = int(input())
b = int(input())
n = int(input())


def gcd(a, b):
    if b == 0:
        return a
    c = a // b
    d = a % b
    return gcd(b, d)


lcm = a * b // gcd(a, b)

print((n + lcm - 1) // lcm * lcm)
