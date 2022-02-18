a, b, c = map(int, input().split())

if a == b == c and a % 2 == 0:
    print(-1)
else:
    res = 0
    while 1:
        if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
            break
        a_, b_, c_ = a, b, c
        a = b_ // 2 + c_ // 2
        b = c_ // 2 + a_ // 2
        c = a_ // 2 + b_ // 2
        res += 1
    print(res)
