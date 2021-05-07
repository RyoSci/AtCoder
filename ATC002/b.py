n, m, p = map(int, input().split())


def cal(n, m, p):
    twice = n
    rest = 1
    while p != 1:
        if p % 2 == 1:
            rest = ((rest % m) * (twice % m)) % m
        twice = ((twice % m) * (twice % m)) % m
        p //= 2

    return twice * rest % m


print(cal(n, m, p))
