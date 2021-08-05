a, b = map(int, input().split())
a -= 1
b -= 1

res = []

for i in range(100):
    tmp = ""
    for j in range(100):
        if i < 50:
            tmp += "."
        else:
            tmp += "#"
    res.append(list(tmp))


for i in range(0, 48, 2):
    for j in range(0, 100, 2):
        if b == 0:
            break
        else:
            res[i][j] = "#"
            b -= 1
    if b == 0:
        break

for i in range(51, 100, 2):
    for j in range(0, 100, 2):
        if a == 0:
            break
        else:
            res[i][j] = "."
            a -= 1
    if a == 0:
        break

print(100, 100)
for i in range(100):
    print(*res[i], sep="")
