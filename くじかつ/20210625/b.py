n = int(input())
a = list(map(int, input().split()))

pre = 0
res = 0
for i in range(n):
    if pre == a[i]:
        res += 1
        pre = a[i]+100
    else:
        pre = a[i]

print(res)
