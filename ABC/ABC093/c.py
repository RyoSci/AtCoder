a, b, c = sorted(list(map(int, input().split())))
ac = c - a
bc = c - b

res = 0
if ac % 2 == 0 and bc % 2 == 0:
    res = ac // 2 + bc // 2
elif ac % 2 == 1 and bc % 2 == 1:
    res = 1 + ac // 2 + bc // 2
else:
    res = 2 + ac // 2 + bc // 2

print(res)
