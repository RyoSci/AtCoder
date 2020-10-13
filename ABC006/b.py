a = [0] * (10 ** 6)
a[2] = 1
mod = 10007
for i in range(3, 10 ** 6):
    a[i] = (a[i - 1] + a[i - 2] + a[i - 3]) % mod

n = int(input())
print(a[n - 1])
