n, k = map(int, input().split())
a = list(map(int, input().split()))

d = dict()
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1


k = max(0, len(d)-k)
val = sorted(d.values())
res = 0
for i in range(k):
    res += val[i]
print(res)
