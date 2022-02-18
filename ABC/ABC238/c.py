import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
mod = 998244353

m = len(str(n))


def f(x):
    return x*(x+1)//2 % mod


ans = 0
now = 0
for i in range(m):
    now = min(n, 10**(i+1)-1)-10**i+1
    ans += f(now)
    ans %= mod

print(ans)
