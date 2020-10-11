n, t = map(int, input().split())
a = [int(input()) for i in range(n)]
total = t
for i in range(1, n):
    total += min(t, a[i]-a[i-1])

print(total)
