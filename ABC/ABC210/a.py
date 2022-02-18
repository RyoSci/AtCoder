n, a, x, y = map(int, input().split())

res = 0
for i in range(1, n+1):
    if i >= a+1:
        res += y
    else:
        res += x

print(res)
