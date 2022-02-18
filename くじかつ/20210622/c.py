x = int(input())

res = x//11*2
if x % 11 > 6:
    res += 2
elif 0 < x % 11 <= 6:
    res += 1

print(res)
