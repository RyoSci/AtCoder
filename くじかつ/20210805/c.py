n = int(input())
x = []
y = []

for i in range(n):
    xi, yi = map(int, input().split())
    x.append([xi, i])
    y.append([yi, i])

x.sort()
y.sort()

dis = []
for z in [x, y]:
    num0, zi = z[0]
    num1, zj = z[-1]
    dis.append([num1-num0, zi, zj])
    num0, zi = z[0]
    num1, zj = z[-2]
    dis.append([num1-num0, zi, zj])
    num0, zi = z[1]
    num1, zj = z[-1]
    dis.append([num1-num0, zi, zj])

dis.sort(reverse=True)

cnt = 0
d = set()
for i in range(6):
    if cnt == 2:
        break
    res, zi, zj = dis[i]
    if (zi, zj) not in d:
        d.add((zi, zj))
        cnt += 1
print(res)
