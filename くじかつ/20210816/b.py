x, y = map(int, input().split())

a = [x]

while 1:
    if a[-1]*2 <= y:
        a.append(a[-1]*2)
    else:
        break

print(len(a))
