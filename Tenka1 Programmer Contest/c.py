N = int(input())
ans = False
for h in range(1, 3501):
    for n in range(1, 3501):
        tmp = 4 * h * n - N * n - N * h
        if tmp == 0:
            continue
        w = N * h * n / tmp
        if w == int(w) and 1 <= w <= 3500:
            ans = (h, n, int(w))
            break
    if ans:
        break

print(*ans)
