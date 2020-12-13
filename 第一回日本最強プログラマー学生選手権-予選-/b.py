n, k = map(int, input().split())
a = list(map(int, input().split()))
first = 0
diff = 0
mod = 10 ** 9 + 7

for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            if i < j:
                first += 1
            diff += 1

res = diff * (k - 1) * k // 2 % mod + k * first % mod
print(res % mod)
