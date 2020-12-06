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
d_sum = sum(d)
j = 0
c_sum = sum(c)
if d_sum + c_sum < 0:
    ans = -1
else:
    while c_sum < 0:
        c_sum += d[j]
        j += 1
        if j >= len(d):
            break
    ans = n - (len(d) - j)

print(ans)
