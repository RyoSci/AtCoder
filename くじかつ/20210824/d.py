n = int(input())
a = list(map(int, input().split()))

m = 0
for i in range(n):
    if a[i] < 0:
        m += 1
res = 0
min_a = 10**18
for i in range(n):
    res += abs(a[i])
    min_a = min(min_a, abs(a[i]))

if m % 2 == 0:
    print(res)
else:
    print(res-2*min_a)
