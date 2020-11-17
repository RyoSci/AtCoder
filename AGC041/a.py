n, a, b = map(int, input().split())
if (b - a) % 2 == 0:
    print((b - a) // 2)
else:
    # if a - 1 < n - b:
    #     res = a - 1 + 1 + (b - a - 1) // 2
    # else:
    #     res = n - b + 1 + (b - a - 1) // 2
    res = min(a - 1, n - b) + 1 + (b - a - 1) // 2
    print(res)
