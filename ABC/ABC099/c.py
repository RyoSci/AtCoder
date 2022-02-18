n = int(input())
counter = 0

while True:
    flag_9 = False
    flag_6 = False

    for i in range(5, 0, -1):
        if n >= 9 ** i:
            n -= 9 ** i
            counter += 1
            break
    else:
        flag_9 = True

    for i in range(6, 0, -1):
        if n >= 6 ** i:
            n -= 6 ** i
            counter += 1
            break
    else:
        flag_6 = True

    if flag_9 and flag_6:
        break

counter += n
print(counter)
