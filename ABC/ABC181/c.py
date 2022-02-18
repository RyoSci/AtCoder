n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

flag = False
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        dx = xy[j][0] - xy[i][0]
        if dx == 0:
            for k in range(j + 1, n):
                if xy[j][0] == xy[k][0]:
                    flag = True
                    break
        else:
            # dy = xy[j][1] - xy[i][1]
            # a = dy / dx
            # b = xy[j][1] - a * xy[j][0]
            # for k in range(j + 1, n):
            #     if xy[k][1] == a * xy[k][0] + b:
            #         flag = True
            #         break
            dy = xy[j][1] - xy[i][1]

            for k in range(j + 1, n):
                if dx * xy[k][1] == dy * xy[k][0] + dx * xy[j][1] - dy * xy[j][0]:
                    flag = True
                    break
        if flag:
            break
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")
