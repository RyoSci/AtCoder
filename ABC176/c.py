n = int(input())
a = list(map(int, input().split()))
now = a[0]
res = 0
for i in range(1, n):
    res += max(0, now - a[i])
    now = max(a[i], now)

print(res)
