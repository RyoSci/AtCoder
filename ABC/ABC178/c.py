n = int(input())
mod = 10 ** 9 + 7
res = (10 ** n) % mod - (2 * 9 ** n) % mod + (8 ** n) % mod
print(res % mod)
