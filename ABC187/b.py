n = int(input())
ans = 0

xy = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        if -1 <= (xy[j][1] - xy[i][1]) / (xy[j][0]-xy[i][0]) <= 1:
            ans += 1

print(ans)
