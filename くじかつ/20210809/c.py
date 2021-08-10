s = input()

w = 0
for i in s:
    if i == "W":
        w += 1

res = 0
for i in s:
    if i == "B":
        res += w
    else:
        w -= 1

print(res)
