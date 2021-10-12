import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

digits = [0]*100
mod = 10**9+7


def f(x):
    res = []
    while x > 0:
        if x % 2 == 1:
            res.append(1)
        else:
            res.append(0)
        x //= 2
    return res


for i in range(n):
    ai = f(a[i])
    for j in range(len(ai)):
        digits[j] += ai[j]

res = 0
two = 1
for i in range(100):
    one = digits[i]
    zero = n-one
    two %= mod
    res += two*one*zero % mod
    res %= mod
    two *= 2

print(res)
