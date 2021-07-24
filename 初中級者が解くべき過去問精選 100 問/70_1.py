m, n = map(int, input().split())
mod = 10**9+7


def cal(x, n):
    tmp = 1
    rest = 1
    while n != 1:
        if n % 2 == 1:
            rest *= x
            rest %= mod
        x = x*x % mod
        n //= 2
    return x*rest % mod


print(cal(m, n))
