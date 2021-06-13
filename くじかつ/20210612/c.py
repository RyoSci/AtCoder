n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append([xi, i])
    y.append([yi, i])

x.sort(reverse=True)
y.sort(reverse=True)
xmax = x[:2]
xmin = x[-2:]
ymax = y[:2]
ymin = y[-2:]

dis = []
for xi, i in xmax:
    for xj, j in xmin:
        dis.append([xi-xj, (i, j)])
for yi, i in ymax:
    for yj, j in ymin:
        dis.append([yi-yj, (i, j)])

dis.sort(reverse=True)
cnt = 0
s = set()

for k, (i, j) in dis:
    if (i, j) not in s:
        cnt += 1
        s.add((i, j))
    if cnt == 2:
        break

print(k)
