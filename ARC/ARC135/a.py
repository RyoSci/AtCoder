import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

mod = 998244353
x = int(input())
x_ = x
for i in range(100):
    if x < 4:
        now = pow(2, i)
        break
    x //= 2

if now == 0:
    print(x)
else:
    rest = x_ % now
    ans = pow(x+1, rest, mod)*pow(x, now-rest, mod)
    ans %= mod

    print(ans)
