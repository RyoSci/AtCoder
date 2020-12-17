a, b = map(int, input().split())


def gcd(a, b):
    while 1:
        c = a % b
        a = b
        b = c
        if b == 0:
            return a


c = gcd(a, b)
div = dict()
div[1] = 1
for i in range(2, 10 ** 6 + 1):
    while c % i == 0:
        c //= i
        div[i] = 1

div[c] = 1

print(len(div))
