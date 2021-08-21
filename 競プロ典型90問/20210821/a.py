a, b, c = map(int, input().split())


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


min_t = gcd(gcd(a, b), c)


def cal(x, y):
    return x//y-1


res = cal(a, min_t)+cal(b, min_t)+cal(c, min_t)
print(res)
