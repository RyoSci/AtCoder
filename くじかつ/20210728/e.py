n = int(input())
a = list(map(int, input().split()))


for i in range(n-1):
    a[i+1] += a[i]

# +-+-
res = 0
pre = 0
for i in range(n):
    if i % 2 == 0:
        if a[i]+pre > 0:
            pre = pre
        else:
            tmp = 1 - (pre+a[i])
            res += tmp
            pre = tmp+pre
    else:
        if a[i]+pre < 0:
            pre = pre
        else:
            tmp = -1 - (pre+a[i])
            res += abs(tmp)
            pre = tmp+pre


# -+-+
res1 = 0
pre = 0
for i in range(n):
    if i % 2 != 0:
        if a[i]+pre > 0:
            pre = pre
        else:
            tmp = 1 - (pre+a[i])
            res1 += tmp
            pre = tmp+pre
    else:
        if a[i]+pre < 0:
            pre = pre
        else:
            tmp = -1 - (pre+a[i])
            res1 += abs(tmp)
            pre = tmp+pre

print(min(res, res1))
