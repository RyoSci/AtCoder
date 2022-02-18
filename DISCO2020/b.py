n = int(input())
a = list(map(int, input().split()))
h = sum(a) / 2

now = 0
for i in range(n):
    if now + a[i] >= h:
        break
    else:
        now += a[i]

# res = 2 * min(h - now, now + a[i] - h)
# print(int(res))
res = min(sum(a) - 2 * now, 2 * (now + a[i]) - sum(a))
print(res)
