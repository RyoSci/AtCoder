n = int(input())
xyh = []
for i in range(n):
    x, y, h = map(int, input().split())
    xyh.append([x, y, h])

xyh.sort(key=lambda x: x[2], reverse=True)

for x in range(101):
    for y in range(101):
        h = -1
        ans = True
        for i in range(n):
            xi, yi, hi = xyh[i]
            if hi == 0:
                if h-abs(xi-x)-abs(yi-y) > 0:
                    ans = False
                    break
            else:
                if h == -1:
                    h = hi+abs(xi-x)+abs(yi-y)
                else:
                    if h != hi+abs(xi-x)+abs(yi-y):
                        ans = False
                        break
        if ans:
            print(x, y, h)
            exit()
