n, m = map(int, input().split())
a = list(map(int, input().split()))

d = dict()

for i in range(n):
    if a[i] not in d:
        d[a[i]] = 0
    d[a[i]] += 1

for i in range(m):
    b, c = map(int, input().split())
    if c not in d:
        d[c] = 0
    d[c] += b

j = 0
d_keys = sorted(list(d.keys()), reverse=True)
res = 0
for i in range(n):
    while 1:
        if d[d_keys[j]] != 0:
            res += d_keys[j]
            d[d_keys[j]] -= 1
            break
        else:
            j += 1

print(res)
