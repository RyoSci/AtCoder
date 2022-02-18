n, c = map(int, input().split())
abc = sorted([list(map(int, input().split())) for _ in range(n)])

endtime_price = dict()
l, r = 0, 10**9
day_price = 0
res = 0
abc = [[0, 0, 0]] + abc
print(abc)
is_over = False
for i in range(1, n+1):

    if abc[i][1] not in endtime_price:
        endtime_price[abc[i][1]] = abc[i][2]
    else:
        endtime_price[abc[i][1]] += abc[i][2]

    if not is_over:
        res += (min(abc[i-1][1], abc[i][0]) - abc[i-1][0]) * abc[i-1][2]
    if l <= abc[i][0] <= r:

        l = max(l, abc[i][0])
        r = min(r, abc[i][1])

        day_price += abc[i][2]
        if day_price >= c:
            res += (r-l+1)*c
            day_price -= endtime_price[r]
            endtime_price[r] = 0
            l = r

            # l, r = r, 10**9
            is_over = True
        else:
            is_over = False

    else:
        if abc[i][2] >= c:
            res += (abc[i][1] - abc[i][0]+1)*c
            is_over = True
        else:
            # res += (abc[i][1] - abc[i][0])*abc[i][2]
            is_over = False

        endtime_price[abc[i][1]] -= abc[i][2]
        l, r = 0, 10**9
        day_price = 0

for endtime, price in endtime_price.items():
    if price != 0:
        res += (endtime-l+1)*price

print(res)
