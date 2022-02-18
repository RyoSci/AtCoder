m = int(input())
if m < 100:
    print("00")
elif m <= 5000:
    m //= 100
    print(str(m).zfill(2))
elif 6000 <= m <= 30000:
    m //= 1000
    m += 50
    print(m)
elif 35000 <= m <= 70000:
    m //= 1000
    m -= 30
    m //= 5
    m += 80
    print(m)
elif 70000 < m:
    print(89)
