n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    a[i] += a[i-1]

d = dict()
d[0] = 1
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 0
    d[a[i]] += 1

res = 0
for val in d.values():
    res += val*(val-1)//2

print(res)
