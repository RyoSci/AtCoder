# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import time
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = 2*10**6 + 100
MOD = 10**9+7
r1, c1, r2, c2 = map(int, input().split())

"""inv使わないVer"""
fact = [1]*(n+1)
invfact = [1]*(n+1)

for i in range(1, n+1):
    fact[i] = i*fact[i-1]
    fact[i] %= MOD

invfact[n] = pow(fact[n], MOD-2, MOD)
for i in range(n, 0, -1):
    invfact[i-1] = invfact[i]*i
    invfact[i-1] %= MOD


def nCk(n, k):
    if k < 0 or n < k:
        return 0
    return fact[n]*invfact[k]*invfact[n-k] % MOD


ans = 0
for j in range(c1, c2+1):
    ans += nCk(r2+j+1, r2)
    ans %= MOD

for j in range(c1, c2+1):
    ans -= nCk(r1-1+j+1, r1-1)
    ans %= MOD

print(ans)
