n = int(input())


def chech10(i):
    i = str(i)
    return "7" in i


def chech8(i):
    tmp = ""
    while True:
        a = i//8
        b = i % 8
        tmp += str(b)
        if a == 0:
            break
        i = a
    return "7" in tmp


res = 0
for i in range(1, n+1):
    if not (chech10(i) or chech8(i)):
        res += 1

print(res)
