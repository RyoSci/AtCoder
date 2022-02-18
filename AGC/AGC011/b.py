n = int(input())
a = list(map(int, input().split()))
a.sort()
checker = 0

for i in range(n - 1):
    if a[i] * 2 < a[i + 1]:
        checker = i + 1
    a[i + 1] += a[i]

print(n - checker)
