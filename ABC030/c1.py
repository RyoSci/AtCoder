n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def binary_search(now, ab):
    l = 0
    r = len(ab) - 1
    while l + 1 != r and r != 0:
        m = (l + r) // 2
        if now == ab[m]:
            r = m
            break
        elif now < ab[m]:
            r = m
        else:
            l = m
    if now <= ab[l]:
        return ab[l]
    elif ab[r] < now:
        return False
    else:
        return ab[r]


now = 0
counter = 0
while 1:
    now = binary_search(now, a)
    if not now:
        break
    else:
        counter += 1
        now += x
    now = binary_search(now, b)
    if not now:
        break
    else:
        counter += 1
        now += y
print(counter // 2)
