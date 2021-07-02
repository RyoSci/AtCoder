n, x = map(int, input().split())
l = list(map(int, input().split()))

res = 1
d = 0
for i in range(n):
    d += l[i]
    if d <= x:
        res += 1
print(res)
