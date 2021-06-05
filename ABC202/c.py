n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

d = dict()
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1

res = 0
for i in range(n):
    if b[c[i]-1] in d:
        res += d[b[c[i]-1]]

print(res)
