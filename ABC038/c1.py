n = int(input())
a = list(map(int, input().split())) + [0]
r = 0
res = 0
for l in range(n):
    r = max(r, l)
    while r <= n:
        if a[r + 1] > a[r]:
            r += 1
        else:
            break
    res += r - l + 1
print(res)
