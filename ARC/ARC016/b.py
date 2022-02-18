n = int(input())
x = [input() for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(9):
        if x[i][j] == "x":
            ans += 1


j = 0
while j < 9:
    tmp = 0
    i = 0
    while i < n:
        if x[i][j] == "o":
            tmp = 1
        else:
            ans += tmp
            tmp = 0
        i += 1
    ans += tmp
    j += 1

print(ans)
