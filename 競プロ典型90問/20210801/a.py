n, k = map(int, input().split())


def cal(x):
    res = 0
    x = str(x)
    for i in range(len(x)):
        res += int(x[i])*8**(len(x)-i-1)
    x = int(res)
    res = ""
    while x > 0:
        tmp = str(x % 9)
        if tmp == "8":
            tmp = "5"
        res += tmp
        x //= 9
    return int(res[::-1])


if n == 0:
    print(0)
else:
    for i in range(k):
        n = cal(n)

    print(n)
