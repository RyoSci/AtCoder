n = int(input())
lr = []
for i in range(n):
    x, l = map(int, input().split())
    lr.append([x-l, x+l])

lr.sort(key=lambda x: x[1])

res = n
pre_r = -10**10
for i in range(n):
    l, r = lr[i]
    if pre_r <= l:
        pre_r = r
    else:
        res -= 1

print(res)
