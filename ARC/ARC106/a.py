n = int(input())
flag = False
for i in range(1, 39):
    for j in range(1, 27):
        if 3 ** i + 5 ** j == n:
            print(i, j)
            flag = True
            break
    if flag:
        break
else:
    print(-1)
