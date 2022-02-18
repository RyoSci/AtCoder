n = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
    while 1:
        div = a // b
        mod = a % b
        if mod == 0:
            return b
        a = b
        b = mod


res = a[0]
for i in range(1, n):
    res = gcd(res, a[i])

print(res)
