n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
koma_pos = [0]

distance = [0] * (m - 1) 
for i in range(m - 1):
    tmp = x[i + 1] - x[i]
    distance[i] = [tmp, i + 1]

distance.sort(reverse=True)

res = 0
for i in range(min(n - 1, len(distance))):
    tmp, index = distance[i]
    koma_pos.append(index)

koma_pos.sort()
koma_pos.append(m)
for i in range(min(n, len(koma_pos) - 1)):
    l = koma_pos[i]
    r = koma_pos[i + 1]
    res += x[r - 1] - x[l]

print(res)
# print(koma_pos)
# print(distance)
# print(x)