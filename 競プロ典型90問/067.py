n, k = map(int, input().split())

if n == 0:
    print(0)

else:
    def eight2nine(x):
        x_ = 0
        x = str(x)[::-1]
        for i in range(len(x)):
            x_ += int(x[i])*8**i
        x = x_

        n = ""
        while x > 0:
            tmp = str(x % 9)
            if tmp == "8":
                tmp = "5"
            n += tmp
            x //= 9
        return int(n[::-1])

    for i in range(k):
        n = eight2nine(n)

    print(n)
