x = int(input())
res = (x // 11) * 2
if 1 <= x % 11 <= 6:
    res += 1
elif 7 <= x % 11 <= 10:
    res += 2
print(res)
