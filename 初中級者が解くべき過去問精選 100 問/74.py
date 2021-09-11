import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
k = int(input())
mod = 10**9+7


def cal(n, k):
    res = 1
    for i in range(n, n-k, -1):
        res *= i
        res %= mod

    for i in range(k, 0, -1):
        res *= pow(i, mod-2, mod)
        res %= mod
    return res


print(cal(n+k-1, k))
