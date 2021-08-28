import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

l, r = map(int, input().split())
mod = 10**9+7


def cal(x):
    n = len(str(x))
    res = 0
    for i in range(1, n):
        res += i*(10**i-1+10**(i-1))*(10**i-1-10**(i-1)+1)//2
        res %= mod

    res += n*(x+10**(n-1))*(x-10**(n-1)+1)//2
    res %= mod
    return res


print((cal(r)-cal(l-1)) % mod)
