n, k = map(int, input().split())
a = list(map(int, input().split()))

d = [[i, 0] for i in range(n)]

for i in range(n):
    d[a[i]-1][1] += 1

num = 0
for i in range(n):
    if d[i][1] != 0:
        num += 1

if num <= k:
    print(0)
else:
    res = 0
    j = 0
    d.sort(key=lambda x: x[1])
    for i in range(num-k):
        while 1:
            if d[j][1] != 0:
                res += d[j][1]
                j += 1
                break
            j += 1
    print(res)
