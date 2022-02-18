n, a, b = map(int, input().split())
mod = 10 ** 9 + 7


def pow(x, n):
    xhat = 1
    while True:
        if n % 2 == 1:
            xhat = xhat * x % mod
        x = x * x % mod
        n //= 2
        if n == 1:
            return x * xhat % mod


res = pow(2, n) - 1

res_a = 1
for i in range(a):
    res_a = res_a * (n - i) * pow(i + 1, mod - 2) % mod

res_b = 1
for i in range(b):
    res_b = res_b * (n - i) * pow(i + 1, mod - 2) % mod

print((res - res_a - res_b) % mod)
