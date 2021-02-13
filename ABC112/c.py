n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]
xyh = sorted(xyh, reverse=True, key=lambda x: x[-1])

for cx in range(101):
    for cy in range(101):
        ans = True
        xi, yi, hi = xyh[0]
        h = hi + abs(xi - cx) + abs(yi - cy)
        for i in range(1, n):
            xi, yi, hi = xyh[i]
            if hi != 0:
                if h != hi + abs(xi - cx) + abs(yi - cy):
                    ans = False
            else:
                if h - abs(xi - cx) - abs(yi - cy) > 0:
                    ans = False
        if ans:
            print(cx, cy, h)
            exit()
