n = int(input())
a = list(map(int, input().split()))


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def cal(x):
    tmp = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            tmp += 1
            if x//i != i:
                tmp += 1
    return tmp


g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])

print(cal(g))
