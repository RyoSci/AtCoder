s = int(input())
a = [s]
i = 1
while True:
    if a[i - 1] % 2 == 0:
        a.append(a[i - 1] // 2)
    else:
        a.append(a[i - 1] * 3 + 1)
    if a.count(a[i]) == 2:
        print(i + 1)
        break
    i += 1
