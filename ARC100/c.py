n = int(input())
a = list(map(int, input().split()))

y0_points = dict()
for i in range(n):
    a[i] = a[i] - (i + 1)
    if a[i] not in y0_points:
        y0_points[a[i]] = 1
    else:
        y0_points[a[i]] += 1

x = sorted(y0_points.keys())

up = 0
down = n
for key in x:
    up += y0_points[key]
    down -= y0_points[key]
    b = key
    if up > down:
        break

ans = 0
for i in range(n):
    ans += abs(a[i] - b)

print(ans）
