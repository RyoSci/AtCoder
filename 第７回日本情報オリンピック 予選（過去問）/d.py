n = int(input())
fig1 = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
fig2 = [list(map(int, input().split())) for _ in range(m)]
fig2_set = set()
for i in range(m):
    fig2_set.add((fig2[i][0], fig2[i][1]))

for i in range(n):
    for j in range(m):
        dx = fig2[j][0]-fig1[i][0]
        dy = fig2[j][1]-fig1[i][1]
        for k in range(n):
            x = fig1[k][0]+dx
            y = fig1[k][1]+dy
            if not (x, y) in fig2_set:
                break
        else:
            ans = (dx, dy)
            print(*ans)
            exit()
