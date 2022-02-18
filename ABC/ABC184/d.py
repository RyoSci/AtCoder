a, b, c = map(int, input().split())


def combination(n, y_num, z_num):
    tmp = 1
    k = y_num+z_num
    for i in range(n, n-k, -1):
        tmp *= i
    for i in range(y_num, 0, -1):
        tmp //= i
    for i in range(z_num, 0, -1):
        tmp //= i
    return tmp


def multiple(x, x_num):
    tmp = 1
    for i in range(x, x+x_num):
        tmp *= i
    return tmp


def f(i, x):
    global ans
    rest = [a, b, c]
    del rest[i]
    x_num = 100-x
    y, z = rest
    for yy in range(y, 100):
        for zz in range(z, 100):
            y_num = yy-y
            z_num = zz-z
            n = x_num+y_num+z_num
            tmp = combination(n-1, y_num, z_num)
            ans += tmp*n*multiple(x, x_num)*multiple(y,
                                                     y_num)*multiple(z, z_num)/multiple(a+b+c, n)


ans = 0
for i, x in enumerate([a, b, c]):
    f(i, x)

print(ans)
