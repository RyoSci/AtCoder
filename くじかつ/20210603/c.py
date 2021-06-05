a, b, c, d = map(int, input().split())


def f(x):
    return b//x - (a+x-1)//x + 1


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(b-a+1-f(c)-f(d)+f(c*d//gcd(c, d)))
