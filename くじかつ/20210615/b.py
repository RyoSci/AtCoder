a = [input().split() for _ in range(3)]
n = int(input())

for i in range(n):
    b = input()
    for j in range(3):
        for k in range(3):
            if a[j][k] == b:
                a[j][k] = "x"

ans = "No"
for i in range(3):
    tmp = 0
    for j in range(3):
        if a[i][j] == "x":
            tmp += 1
    if tmp == 3:
        ans = "Yes"
for j in range(3):
    tmp = 0
    for i in range(3):
        if a[i][j] == "x":
            tmp += 1
    if tmp == 3:
        ans = "Yes"
tmp = 0
for i in range(3):
    if a[i][i] == "x":
        tmp += 1
if tmp == 3:
    ans = "Yes"
tmp = 0
for i in range(3):
    if a[2-i][i] == "x":
        tmp += 1
if tmp == 3:
    ans = "Yes"

print(ans)
