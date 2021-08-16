n, m = map(int, input().split())
p_cy = [[] for _ in range(n)]

for i in range(m):
    p, y = map(int, input().split())
    p_cy[p-1].append([y, i])

ans = [0]*m
for i in range(n):
    p_cy[i].sort()
    for j, (y, ii) in enumerate(p_cy[i]):
        ans[ii] = str(i+1).zfill(6)+str(j+1).zfill(6)

for i in range(m):
    print(ans[i])
