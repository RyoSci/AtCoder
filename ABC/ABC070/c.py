n = int(input())
t = [int(input()) for _ in range(n)]


def gcd(a, b):
    while 1:
        mod = a % b
        if mod == 0:
            return b
        a = b
        b = mod


res = t[0]
for i in range(1, n):
    res = res * t[i] // gcd(res, t[i])

print(res)
