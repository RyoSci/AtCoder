n = int(input())


def cal(x):
    res = 0
    x = x[::-1]
    for i in range(len(x)):
        res += x[i]*10**i

    return res


def f(x):
    for i in range(20):
        if x < 10**i*(10**i+1)//2:
            break
    b = [9]*i
    for j in range(i):
        while 1:
            tmp = cal(b)
            if tmp*(tmp+1)//2 <= x:
                b[j] += 1
                break
            b[j] -= 1
    return cal(b)-1


# def f(x):
#     for i in range(10**9):
#         if i*(i+1)//2 > x:
#             return i-1


k = f(n+1)

print(1+n-k)
