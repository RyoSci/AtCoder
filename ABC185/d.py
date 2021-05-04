n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
left = 0
white = []
for i in range(m):
    tmp = a[i]-1-left
    if tmp > 0:
        white.append(tmp)
    left = a[i]
tmp = n-left
if tmp > 0:
    white.append(tmp)

if len(white) == 0:
    res = 0
else:
    stamp = min(white)

    res = 0
    for i in white:
        res += (i+stamp-1)//stamp

print(res)
