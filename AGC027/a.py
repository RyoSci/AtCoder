n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
res = 0
for i in range(n):
    if x >= a[i]:
        res += 1
        x -= a[i]
    else:
        break
if x != 0 and res == n:
    res = res - 1

print(res)
