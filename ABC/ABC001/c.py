from decimal import Decimal, ROUND_HALF_UP
deg, dis = map(int, input().split())
dis /= 60
dis = Decimal(str(dis)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
dis = float(dis)

if 0.0 <= dis <= 0.2:
    w = 0
elif dis <= 1.5:
    w = 1
elif dis <= 3.3:
    w = 2
elif dis <= 5.4:
    w = 3
elif dis <= 7.9:
    w = 4
elif dis <= 10.7:
    w = 5
elif dis <= 13.8:
    w = 6
elif dis <= 17.1:
    w = 7
elif dis <= 20.7:
    w = 8
elif dis <= 24.4:
    w = 9
elif dis <= 28.4:
    w = 10
elif dis <= 32.6:
    w = 11
elif 32.7 <= dis:
    w = 12

if w == 0:
    dir = "C"
else:
    degs = [[112.5+225 * i, 337.5+225 * i] for i in range(15)]
    dirs = ["NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    for id, (i, j) in enumerate(degs):
        if i <= deg < j:
            dir = dirs[id]
            break
    else:
        dir = "N"

print(dir, w)
