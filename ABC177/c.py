n = int(input())
a = list(map(int, input().split()))
sum_a = a[0]
res = 0
mod = 10 ** 9 + 7

for i in range(1, n):
    res = (res + ((sum_a % mod) * (a[i] % mod)) % mod) % mod
    sum_a = (sum_a + a[i]) % mod

print(res % mod)
