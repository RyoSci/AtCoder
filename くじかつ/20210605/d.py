n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))


def bineary_serch_ab(a, bi):
    l = 0
    r = len(a)-1
    m = (l+r)//2
    while l+1 < r:
        if a[m] < bi:
            l = m
        else:
            r = m
        m = (l+r)//2
    if bi <= a[l]:
        return l
    elif a[l] < bi <= a[r]:
        return l+1
    elif a[r] < bi:
        return r+1


def bineary_serch_cb(c, bi):
    l = 0
    r = len(c)-1
    m = (l+r)//2
    while l+1 < r:
        if c[m] <= bi:
            l = m
        else:
            r = m
        m = (l+r)//2
    if bi < c[l]:
        return len(c) - l
    elif c[l] <= bi < c[r]:
        return len(c) - (l+1)
    elif c[r] <= bi:
        return len(c) - (r+1)


res = 0
for i in range(n):
    res += bineary_serch_ab(a, b[i])*bineary_serch_cb(c, b[i])

print(res)
