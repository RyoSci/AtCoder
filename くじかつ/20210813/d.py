n, k = map(int, input().split())
mod = 10**9+7


def f(n, k):
    res = 1
    n, k = n+k, min(n, k)
    for i in range(n, n-k, -1):
        res *= i
        res %= mod

    for i in range(k, 0, -1):
        res *= pow(i, mod-2, mod)
        res %= mod

    return res


for i in range(k):
    red = n-k-i
    blue = k-i-1
    if red < 0 or blue < 0:
        res = 0
    else:
        res = f(blue, i)*f(red, i+1)
    print(res % mod)
