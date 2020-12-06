n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
d = []

for i in range(n):
    tmp = a[i] - b[i]
    if tmp < 0:
        c.append(tmp)
    else:
        d.append(tmp)

d.sort(reverse=True)
d_ = d[::]
j = 0
is_break = False
for i in range(len(c)):
    while c[i] != 0:
        tmp = min(-c[i], d[j])
        c[i] += tmp
        d[j] -= tmp
        if d[j] == 0:
            j += 1
        if j >= len(d):
            is_break = True
            break
    if is_break:
        break

ans = 0
for i in range(len(d)):
    if d[i] == d_[i]:
        ans += 1

if c != [] and c[-1] < 0:
    print(-1)
else:
    print(n - ans)
