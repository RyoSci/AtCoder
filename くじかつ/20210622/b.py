k = int(input())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


res = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        tmp = gcd(a, b)
        for c in range(1, k+1):
            res += gcd(tmp, c)

print(res)
