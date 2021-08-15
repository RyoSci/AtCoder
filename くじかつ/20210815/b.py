n = int(input())

for i in range(n, 1000):
    i = str(i)
    if i[0] == i[1] == i[2]:
        print(i)
        break
