w, h = map(int, input().split())

mod = 10**9+7


def cal(n, k):
    n, k = sorted([n, k])
    n -= 1
    k -= 1
    tmp = 1
    for i in range(n+k, k, -1):
        tmp *= i
        tmp %= mod
    for i in range(n, 0, -1):
        tmp *= pow(i, mod-2, mod)
        tmp %= mod
    return tmp


print(cal(w, h))
