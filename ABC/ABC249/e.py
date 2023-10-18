# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, p = map(int, input().split())

fac = [1] + [1]
finv = [1] + [1]
inv = [0] + [1]

for i in range(2, 10**5):
    fac += [fac[-1] * i % p]
    inv += [p - inv[p % i] * (p // i) % p]
    finv += [finv[-1] * inv[i] % p]


def comb(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * finv[k] * finv[n-k] % p


ans = 0
m = (n+1)//2-1
for i in range(m, 0, -1):
    now = 26
    for j in range(i-1):
        now *= 25
        now %= p
    ans += now*comb(n-i+1, i-1)
    ans %= p

print(ans)
