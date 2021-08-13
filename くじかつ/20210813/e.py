n, t = map(int, input().split())
a = list(map(int, input().split()))

max_a = [0]*n
max_a[-1] = a[-1]
for i in range(n-1, 0, -1):
    max_a[i-1] = max(a[i-1], max_a[i])

d = dict()
for i in range(n-1):
    tmp = max_a[i+1]-a[i]
    if tmp not in d:
        d[tmp] = 0
    d[tmp] += 1

res = 0
res_i = -1
for key, val in d.items():
    if res < key:
        res_i = val
        res = key

print(res_i)
