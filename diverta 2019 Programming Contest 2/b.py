n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]
dis_map = dict()
for i in range(n - 1):
    for j in range(i + 1, n):
        if xy[i][0] < xy[j][0]:
            tmp_xy = (xy[j][0] - xy[i][0], xy[j][1] - xy[i][1])
        elif xy[i][0] == xy[j][0]:
            tmp_xy = (xy[j][0] - xy[i][0], abs(xy[j][1] - xy[i][1]))
        else:
            tmp_xy = (xy[i][0] - xy[j][0], xy[i][1] - xy[j][1])
        if tmp_xy not in dis_map:
            dis_map[tmp_xy] = 1
        else:
            dis_map[tmp_xy] += 1

if n != 1:
    print(n - max(dis_map.values()))
else:
    print(1)
