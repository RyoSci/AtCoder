n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(int, input().split())) for _ in range(k)]

res = 0
for i in range(1 << k):
    dish = [0]*n
    for j in range(k):
        if i >> j & 1:
            dish[cd[j][0]-1] += 1
        else:
            dish[cd[j][1]-1] += 1
    tmp = 0
    for j in range(m):
        if dish[ab[j][0]-1] > 0 and dish[ab[j][1]-1] > 0:
            tmp += 1

    res = max(res, tmp)

print(res)
