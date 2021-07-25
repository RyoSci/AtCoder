x, y = map(int, input().split())

flag = False
for i in range(10**6+1):
    xx = x-i
    yy = y-i*2
    if xx == 0 and yy == 0:
        flag = True
        j = 0
        break
    elif xx > 0 and yy > 0 and xx % yy == 0 and xx/yy == 2:
        flag = True
        j = xx//2
        break

mod = 10**9+7


def cal(n, k):
    n, k = min(n, k), max(n, k)
    tmp = 1
    for i in range(n+k, k, -1):
        tmp *= i
        tmp %= mod
    for i in range(n, 0, -1):
        tmp *= pow(i, mod-2, mod)
        tmp %= mod
    return tmp


if flag:
    print(cal(i, j))

else:
    print(0)
