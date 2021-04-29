import math
t = int(input())
l, x, y = map(int, input().split())
q = int(input())


def time2yz(e):
    sita = math.radians(360 - (90 + (e / t) * 360) % 360)
    a = math.cos(sita) * l / 2
    b = (math.sin(sita) + 1) * l / 2
    return a, b


def cal_sita(a, b, x, y):
    i = (x ** 2 + (y - a) ** 2 + b ** 2)
    j = (x ** 2 + (y - a) ** 2)
    k = (b ** 2)
    cos_sita = (i + j - k) / (2 * i ** (0.5) * j ** (0.5))
    # print(cos_sita)
    sita = math.acos(cos_sita)
    return math.degrees(sita)


for _ in range(q):
    e = int(input())
    a, b = time2yz(e)
    # print(a, b)
    print(cal_sita(a, b, x, y))
