l, x, y, s, d = map(int, input().split())

clock_dis = (d - s) % l
res = clock_dis / (x + y)
counterclock_dis = (s - d) % l
if y - x > 0:
    res = min(res, counterclock_dis / (y - x))
print(res)
