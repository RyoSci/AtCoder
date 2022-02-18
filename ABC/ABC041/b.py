a, b, c = map(int, input().split())
mod = 10 ** 9 + 7
res = a % mod * b % mod * c % mod
print(res % mod)
