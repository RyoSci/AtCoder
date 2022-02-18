y, m, d = map(int, input().split("/"))


def chech_leap(y):
    ans = "NO"
    if y % 400 == 0:
        ans = "YES"
    elif y % 100 == 0:
        ans = "NO"
    elif y % 4 == 0:
        ans = "YES"
    return ans


thirty = set([4, 6, 9, 11])
thirty_one = set([1, 3, 5, 7, 8, 10])
ans = ""
for i in range(2000 * 366):
    if y % (m * d) == 0:
        ans = r"%s/%s/%s" % (y, str(m).zfill(2), str(d).zfill(2))
        break
    d += 1

    if m in thirty and d == 31:
        d %= 30
        m += 1
    elif m in thirty_one and d == 32:
        d %= 31
        m += 1
    elif m == 12 and d == 32:
        d %= 31
        m = 1
        y += 1
    elif m == 2:
        if chech_leap(y) == "YES" and d == 30:
            d = 1
            m += 1
        elif chech_leap(y) == "NO" and d == 29:
            d = 1
            m += 1

print(ans)
