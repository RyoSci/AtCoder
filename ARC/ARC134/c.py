import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 998244353

for i in range(1, n):
    a[0] -= a[i]


if a[0] < k:
    print(0)
    exit()
a[0] -= k


def f(k, y):
    res = 1
    for i in range(k-1):
        res = res * ((k-1+y-i) % mod) % mod
    for i in range(1, k):
        res = res*pow(i, mod-2, mod) % mod
    return res


ans = 1
for i in range(n):
    ans = ans*f(k, a[i])
    ans %= mod
print(ans % mod)
