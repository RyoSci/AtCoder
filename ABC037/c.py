n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
for i in range(n):
    a[i + 1] += a[i]

res = 0
for i in range(n - k + 1):
    res += a[i + k] - a[i]

print(res)
