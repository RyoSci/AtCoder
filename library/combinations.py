n = 2*10**5
MOD = 10**9+7

""""""
fact = [1]*(n+1)
inv = [1]*(n+1)
invfact = [1]*(n+1)

for i in range(1, n+1):
    fact[i] = i*fact[i-1]
    fact[i] %= MOD

for i in range(1, n+1):
    inv[i] = pow(i, MOD-2, MOD)

for i in range(1, n+1):
    invfact[i] = invfact[i-1]*inv[i]
    invfact[i] %= MOD


def nCk(n, k):
    if k < 0 or n < k:
        return 0
    return fact[n]*invfact[k]*invfact[n-k] % MOD


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
