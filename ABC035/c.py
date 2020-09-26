n, q = map(int, input().split())
a = [0] * (n + 1)
for i in range(q):
    l, r = map(int, input().split())
    a[l - 1] += 1
    a[r] -= 1

res = ""
for i in range(n):
    a[i + 1] += a[i]
    res += str(a[i] % 2)
print(res)
