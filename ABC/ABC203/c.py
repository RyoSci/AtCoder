n, k = map(int, input().split())


ab = dict()
for i in range(n):
    a, b = map(int, input().split())
    if a not in ab:
        ab[a] = b
    else:
        ab[a] += b

ab_keys = sorted(list(ab.keys()))

res = 0
pre = 0
for i in range(len(ab_keys)):
    a = ab_keys[i]
    b = ab[ab_keys[i]]
    if k >= a - pre:
        k = k-(a - pre)+b
        res += (a - pre)
        pre = a
    else:
        res += k
        k = 0
        break

res += k
print(res)
