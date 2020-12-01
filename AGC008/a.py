x, y = map(int, input().split())
res = 0
if abs(x) <= abs(y):
    if x < 0:
        x *= -1
        res += 1
    tmp = abs(y) - abs(x)
    x += tmp
    res += tmp
else:
    if x >= 0:
        x *= -1
        res += 1
    tmp = abs(x) - abs(y)
    x += tmp
    res += tmp

if x != y:
    res += 1

print(res)
