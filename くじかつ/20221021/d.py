# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
MOD = 10**9+7

fact = [1]*(n+1)
invfact = [1]*(n+1)

for i in range(1, n+1):
    fact[i] = i*fact[i-1]
    fact[i] %= MOD
invfact[n] = pow(fact[n], MOD-2, MOD)
for i in range(n, 0, -1):
    invfact[i-1] = invfact[i]*i
    invfact[i] %= MOD


def nCk(n, k):
    if k < 0 or n < k:
        return 0
    return fact[n]*invfact[k]*invfact[n-k] % MOD


ans = []
for i in range(k):
    # 仕切りにi個使う
    r = n-k-i

    # i個の仕切りに先に1ずつ分配する
    if i > 0:
        b = k-i-1
    else:
        b = k

    # 残りのbを仕切りに分配
    res = nCk(b+i, i)

    # 残りのaを仕切りに分配
    res *= nCk(r+i+1, r) % MOD
    res %= MOD

    ans.append(res)

print(*ans, sep="\n")
