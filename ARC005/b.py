x, y, w = input().split()
x, y = int(x) - 1, int(y) - 1

c = [input() for _ in range(9)]
# x, y, w = 8, 8, "RD"
# c = [[] for _ in range(9)]
# for i in range(81):
#     c[i // 9].append(str(i))
    


directions = [0, 0]
for wi in w:
    if wi == "R":
        directions[0] = 1
    elif wi == "L":
        directions[0] = -1
    elif wi == "U":
        directions[1] = -1
    elif wi == "D":
        directions[1] = 1



ans = ""
for i in range(4):
    ans += c[y][x]
    if x  == 0 and directions[0] == -1 or x  == 8 and directions[0] == 1:
        directions[0] *= -1
    if y  == 0 and directions[1] == -1 or y  == 8 and directions[1] == 1:
        directions[1] *= -1
    x += directions[0]
    y += directions[1]
    
print(ans)