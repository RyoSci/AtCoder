n = int(input())
a = list(map(int, input().split()))


res = -10 ** 5
for i in range(n):
    aoki_max = -10 ** 5
    taka_max = -10 ** 5
    for j in range(n):
        if i == j:
            continue
        ii = min(i, j)
        jj = max(i, j)
        taka = 0
        aoki = 0
        for k in range(ii, jj + 1):
            if (k - ii + 1) % 2 == 1:
                taka += a[k]
            else:
                aoki += a[k]
        if aoki_max < aoki:
            aoki_max = aoki
            taka_max = taka
    res = max(taka_max, res)
print(res)
