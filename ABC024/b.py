n, t = map(int, input().split())
a = [int(input()) for i in range(n)]
total = t
for i in range(1, n):
    if a[i] - a[i - 1] > t:
        total += t
    else:
        total += a[i] - a[i - 1]

print(total)
