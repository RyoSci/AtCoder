xa, ya, xb, yb, t, v = map(int, input().split())
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    dis = ((xa - x) ** 2 + (ya - y) ** 2) ** 0.5 + \
        ((xb - x) ** 2 + (yb - y) ** 2) ** 0.5
    if dis <= t * v:
        print("YES")
        break
else:
    print("NO")
