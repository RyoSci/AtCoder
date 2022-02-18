n = int(input())
a = sorted(list(map(int, input().split())))
an = a[-1]
a = a[:n - 1]
res = 10 ** 9
ans = 0
if an % 2 == 0:
    mid_l = an // 2
    mid_r = an // 2
else:
    mid_l = an // 2
    mid_r = (an + 1) // 2

for i in range(n - 1):
    if a[i] <= mid_l:
        if mid_l - a[i] < res:
            ans = a[i]
            res = mid_l - a[i]
    elif mid_r <= a[i]:
        if a[i] - mid_r < res:
            ans = a[i]
            res = mid_r - a[i]

print(an, ans)
