n, x, m = map(int, input().split())
a = [0] * (m + 1)
a[0] = x
double_check = set()
num = -1
i = 0
for i in range(1, n):
    if ((a[i - 1] % m) ** 2) % m not in double_check:
        a[i] = ((a[i - 1] % m) ** 2) % m
        double_check.add(((a[i - 1] % m) ** 2) % m)
    else:
        num = ((a[i - 1] % m) ** 2) % m
        break

res = 0
for j in range(n):
    if a[j] == num:
        break
    res += a[j]

res += (n - j) // (max(1, i - j)) * sum(a[j:i])
res += sum(a[j:j + (n - j) % (max(1, i - j))])

print(res)
