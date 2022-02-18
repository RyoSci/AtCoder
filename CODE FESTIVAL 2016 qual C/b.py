k, t = map(int, input().split())
a = list(map(int, input().split()))
# k = 10000
# t = 100
# a = [10000 // 100] * 100

for i in range(t):
    a[i] = [a[i], i]
a = a + [[0, 0]]
res = 0
pre = -1
for i in range(k):
    a.sort(reverse=True)
    if a[0][1] != pre:
        a[0][0] -= 1
        pre = a[0][1]
    else:
        if a[1][0] == 0:
            a[0][0] -= 1
            res += 1
            pre = a[0][1]
        else:
            a[1][0] -= 1
            pre = a[1][1]

print(res)
