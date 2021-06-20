n, k = map(int, input().split())
mod = 10**9+7


def pow(a, b, mod, rest):
    if b == 1:
        return a*rest % mod
    if b % 2 == 1:
        rest = rest*a % mod
    return pow(a*a % mod, b//2, mod, rest)


if n == 1:
    ans = k
elif n == 2:
    ans = (k*(k-1)) % mod
else:
    ans = (k*(k-1)) % mod
    ans = ans*pow(k-2, n-2, mod, 1) % mod

print(ans)
