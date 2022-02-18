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

d_k = sorted(d.keys(), reverse=True)

res = 0
for key in d_k:
    val = d[key]
    if val >= n:
        res += key*n
        n = 0
        break
    else:
        res += key*val
        n -= val

print(res)
