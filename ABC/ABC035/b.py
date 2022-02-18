s = input()
t = int(input())
q = 0
x = 0
y = 0
for i in s:
    if i == "L":
        x -= 1
    elif i == "R":
        x += 1
    elif i == "U":
        y += 1
    elif i == "D":
        y -= 1
    else:
        q += 1

if t == 1:
    print(abs(x) + abs(y) + q)
else:
    if abs(x) + abs(y) >= q:
        print(abs(x) + abs(y) - q)
    else:
        print((q - abs(x) - abs(y)) % 2)
