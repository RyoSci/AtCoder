c = [input().split() for i in range(4)]

for i in range(4):
    tmp = ""
    for j in range(4):
        tmp += c[3 - i][3 - j]
        if j == 3:
            pass
        else:
            tmp += " "

    print(tmp)
