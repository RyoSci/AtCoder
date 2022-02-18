k = int(input())


def reverce(a, b, i):
    if i == 0:
        return a, b
    a, b = a + b, a
    return reverce(a, b, i - 1)


print(*reverce(2, 1, k - 1))

# a, b = reverce(2, 1, k - 1)


# def gcd(a, b, i):
#     if a % b == 0:
#         return b, i
#     return gcd(b, a % b, i + 1)


# print(gcd(a, b, 1))
