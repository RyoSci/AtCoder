month_has_days = [0] * 13
for i in range(1, 13):
    if i == 1:
        month_has_days[i] = 31
    elif i == 2:
        month_has_days[i] += month_has_days[i - 1] + 29
    elif i in (4, 6, 9, 11):
        month_has_days[i] += month_has_days[i - 1] + 30
    else:
        month_has_days[i] += month_has_days[i - 1] + 31


is_holiday = [0] * 367
for i in range(1, 367):
    if i % 7 == 0 or i % 7 == 1:
        is_holiday[i] = 1

n = int(input())
for i in range(n):
    m, d = map(int, input().split("/"))
    days = month_has_days[m - 1] + d
    while days < 367:
        if is_holiday[days] == 0:
            is_holiday[days] = 1
            break
        else:
            days += 1

ans = 0
now = 0
for i in range(367):
    if is_holiday[i] == 1:
        now += 1
    else:
        ans = max(ans, now)
        now = 0
print(max(ans, now))
