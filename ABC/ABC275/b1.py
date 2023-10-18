# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b, c, d, e, f = list(map(int, input().split()))
MOD = 998244353


def g(x, y, z):
    return (x % MOD) * (y % MOD) * (z % MOD)


ans = g(a, b, c) % MOD - g(d, e, f) % MOD
ans %= MOD
print(ans)
