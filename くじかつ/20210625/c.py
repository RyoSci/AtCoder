a, b, c = map(int, input().split())
a %= 10


def mod(x):
    tmp = x
    d = 0
    while 1:
        d += 1
        tmp = tmp*x % 10
        if x == tmp:
            break
    return d


d = mod(a)
if pow(b % d, c, d) == 0:
    res = a**d % 10
else:
    res = a**pow(b % d, c, d) % 10
print(res)
