a, b, c = map(int, input().split())
mod = 998244353
res = (a + 1) * a // 2 % mod * (b + 1) * b // 2 % mod * (c + 1) * c // 2 % mod
print(res % mod)
