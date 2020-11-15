x = int(input())
if x < 100:
    print(0)
elif x >= 2000:
    print(1)
else:
    num = x // 100
    if num * 100 <= x <= num * 105:
        print(1)
    else:
        print(0)
