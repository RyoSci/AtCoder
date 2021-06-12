s = input()
d = []

for i in s:
    if i == "B":
        if len(d) != 0:
            d.pop()
    else:
        d.append(i)

print(*d, sep="")
