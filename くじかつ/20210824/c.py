n = int(input())
a = list(map(int, input().split()))
d = dict()

for i in range(n):
    if a[i] not in d:
        d[a[i]] = 0
    d[a[i]] += 1


res = 0
for key, val in d.items():
    if key <= val:
        res += val-key
    else:
        res += val

print(res)
