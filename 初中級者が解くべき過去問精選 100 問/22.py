p = float(input())

INF = 10**18


def pow(x, y):
    tmp = 1
    rest = 1
    # rest = x**(y % 1)
    # y = int(y)
    while y > 0:
        if y % 2 != 0:
            rest *= x**(y % 2)
        y //= 2
        if y == 0:
            break
        tmp *= x
        if tmp*rest > INF:
            return INF
    return tmp*rest


def cal(x):
    return p/pow(2, (x/1.5))+x


res = cal(p)


def binary_serch(l, r):
    global res
    for i in range(100):
        m = l+r
        m /= 2
        if cal(m) < res:
            res = cal(m)
            r = m
        else:
            l = m
    return res


print(binary_serch(0, p))
