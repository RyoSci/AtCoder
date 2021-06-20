n, k = map(int, input().split())
mod = 10**9+7
if n == 1:
    ans = k
elif n == 2:
    ans = (k*(k-1)) % mod
else:
    ans = (k*(k-1)) % mod
    ans = ans*pow(k-2, n-2, mod) % mod

print(ans)
