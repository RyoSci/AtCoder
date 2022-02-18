n, k = map(int, input().split())
c = list(map(int, input().split()))
d = dict()
for i in range(k):
    if c[i] not in d:
        d[c[i]] = 0
    d[c[i]] += 1

res = len(d)

for i in range(k, n):
    d[c[i-k]] -= 1
    if d[c[i-k]] == 0:
        del d[c[i-k]]
    if c[i] not in d:
        d[c[i]] = 0
        res = max(res, len(d))
    d[c[i]] += 1

print(res)
